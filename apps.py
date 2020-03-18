# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class EasypaisaModuleConfig(AppConfig):
    name = 'easypaisa_module'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'dev',
            'USER': 'root',
            'PASSWORD': 'dev@Easypaisa.com.pk',
            'HOST': '147.139.31.164',
            'PORT': '3366',
        }
    }