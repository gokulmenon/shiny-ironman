# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.conf import settings
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from disposable_email_checker import DisposableEmailChecker

from .models import User

RESERVED_username_LIST = r'^%s$' % getattr(settings, "RESERVED_username_LIST", '')


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username, username and
    password.
    """
    error_messages = {
        'duplicate_email': _("A user with that email already exists."),
        'duplicate_username': _("A user with that username already exists."),
        'reserved_username': _("That username cannot be used."),
    }
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex='^\w+$',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': _("Username"),
                                     'required': ''}),
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters and numbers.")})
    email = forms.EmailField(
        label=_("E-mail"), max_length=75,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': _("E-mail"),
                                     'required': ''}),
        help_text=_("Required. Valid active e-mail addresses only."),
        error_messages={
            'invalid': _("This value may contain only valid e-mail addresses only.")})
    password = forms.CharField(label=_("password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                     'placeholder': _("Password"),
                                     'required': ''}))

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]

        if username in RESERVED_username_LIST:
            raise forms.ValidationError(self.error_messages['reserved_username'])

        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_email(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]

        email_checker = DisposableEmailChecker()
        if email_checker.is_disposable(email):
            raise forms.ValidationError(_("Registration using disposable email addresses is prohibited. \
            Please supply a different email address."))

        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_email'])

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    error_messages = {
        'invalid_username': _("That username cannot be used."),
    }
    username = forms.CharField(
        label=_("Username"), max_length=30,
        help_text=_("Required. 30 characters or fewer. Letters and digits only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    email = forms.EmailField(label=_("E-mail"), max_length=75)
    password = ReadOnlyPasswordHashField(label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))
    about = forms.CharField(
        label=_("About"), max_length=500, required=False,
        widget=forms.Textarea(attrs={'placeholder': _('About'), 'class': 'form-control', 'style': 'resize: none;'}))

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_email(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]

        email_checker = DisposableEmailChecker()
        if email_checker.is_disposable(email):
            raise forms.ValidationError(_("Registration using disposable email addresses is prohibited. \
            Please supply a different email address."))
        return email

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]

        if username in RESERVED_username_LIST:
            raise forms.ValidationError(self.error_messages['invalid_username'])
        return username

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class SimpleUserChangeForm(forms.ModelForm):
    error_messages = {
        'invalid_username': "Error in clean_username",
    }
    image = forms.ImageField(
        label=_("Image"),
        max_length=200,
        required=False)
    username = forms.RegexField(
        label=_("Username"), max_length=30, regex='^\w+$',
        widget=forms.TextInput(attrs={'placeholder': _('Username'), 'class': 'form-control'}),
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    about = forms.CharField(
        label=_("About"), max_length=500, required=False,
        widget=forms.Textarea(attrs={'placeholder': _('About'), 'class': 'form-control', 'style': 'resize: none;'}))

    class Meta:
        model = User
        fields = ['image', 'username', 'username', 'about']

    def __init__(self, *args, **kwargs):
        super(SimpleUserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]

        if username in RESERVED_username_LIST:
            raise forms.ValidationError(self.error_messages['invalid_username'])
        return username

    def clean_image(self):
        image = self.cleaned_data.get('image',False)
        if image:
            if image.size > 1048576:# 1MB = 1024*1024
                raise forms.ValidationError(_("Image file too large ( > 1 MB )"))
        return image


class RegistrationForm(UserCreationForm):

    tos = forms.BooleanField(widget=forms.CheckboxInput,
                             label=_(u'I have read and agree to the Terms of Service'),
                             error_messages={'required': _("You must agree to the terms to register")})