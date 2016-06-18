from .common import *

print("Dev settings loaded")

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

STATIC_URL = '/comeo_project/comeo_app/static/'
MEDIA_ROOT = '/Users/ipostolaki/envs/comeo_sync/comeo_project/media'

STATIC_ROOT = '/Users/ipostolaki/envs/comeo_sync/comeo_project/comeo_app/static/ROOT'

INSTALLED_APPS += ('debug_toolbar', 'django_extensions',)

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'email-dummy/'

CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_IMAGE_BACKEND = "pillow"

# ipython
# SHELL_PLUS_PRE_IMPORTS = (
#     ('module.submodule1', ('class1', 'function2')),
#     ('module.submodule2', 'function3'),
#     ('module.submodule3', '*'),
#     'module.submodule4'
# )
