/*
* Resend email verification
*/
$(document).on('click', '.email_verification', function(event) {
    var button = $(this);

    button.attr('disabled', 'disabled');

    $.ajax({
        type: "GET",
        url: email_verification_url,
        dataType: 'json',
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(data, status){
            if(data['sent']) {
                button.removeClass('btn-default').addClass('btn-success').html(email_verification_sent);
            }
        },
        error: function(xhr,err){
            alert("Error");
            button.removeAttr('disabled');
        }
    });
});