import os

from django.conf import settings


SLACK_CLIENT_ID = getattr(settings, '583090280038.582728420791', os.environ.get('583090280038.582728420791'))
SLACK_CLIENT_SECRET =  getattr(settings, 'f3ff45e64de27f41b735c9617369f2e2', os.environ.get('f3ff45e64de27f41b735c9617369f2e2'))
SLACK_VERIFICATION_TOKEN = getattr(settings, 'b25MjNbzg0FqCW0dQ048UmoT', os.environ.get('b25MjNbzg0FqCW0dQ048UmoT'))
REST_FRAMEWORK = getattr(settings, 'REST_FRAMEWORK', {'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'})