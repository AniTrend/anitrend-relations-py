"""
Django settings for app project in development env

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from .common import *


DATA_UPLOAD_MAX_NUMBER_FIELDS = 1500

Q_CLUSTER = {
    "name": "relations-sync",
    "orm": "default",
    'workers': 2,
    "recycle": 250,
    "timeout": 1800,
    "retry": 3600,
    "label": "worker",
}

LANGUAGE_CODE = "en-uk"

TIME_ZONE = "Africa/Johannesburg"