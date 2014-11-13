#!/usr/bin/env python
import os

PIPELINE_YUGLIFY_BINARY = './node_modules/yuglify/bin/yuglify'

if (os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or os.getenv('SETTINGS_MODE') == 'prod'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gluwa.settings.production")
    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
    STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
else:
    STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_CSS = {
    'base': {
        'source_filenames': (
            'flat-ui/css/flat-ui.css',
            'css/base.css',
            'font/ChunkFive/chunkfive.css',
        ),
        'output_filename': 'pipeline/css/base.css',
    },
    'home': {
        'source_filenames': (
            'css/home/mobile_home.css',
            'css/home/home.css',
        ),
        'output_filename': 'pipeline/css/home.css',
    },
    'portfolio_list': {
        'source_filenames': (
            'portfolios/css/portfolio_list.css',
        ),
        'output_filename': 'pipeline/portfolios/css/portfolio_list.css',
    },
    'portfolio_detail': {
        'source_filenames': (
            'portfolios/css/portfolio_detail.css',
        ),
        'output_filename': 'pipeline/portfolios/css/portfolio_detail.css',
    },
    'user_detail': {
        'source_filenames': (
            'gluwa_user/css/user_detail.css',
        ),
        'output_filename': 'pipeline/gluwa_user/css/user_detail.css',
    },
    'user_form': {
        'source_filenames': (
            'gluwa_user/css/user_form.css',
        ),
        'output_filename': 'pipeline/gluwa_user/css/user_form.css',
    },
}

PIPELINE_JS = {
    'base': {
        'source_filenames': (
            'js/jquery.placeholder.min.js',
            'js/jquery.livequery.js',
            'js/timeago/jquery.timeago.js',
        ),
        'output_filename': 'pipeline/js/base.js',
    },
    'jquery_timeago_ko': {
        'source_filenames': (
            'js/timeago/jquery.timeago.ko.js',
        ),
        'output_filename': 'pipeline/js/timeago/jquery.timeago.ko.js',
    },
}