from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from slack_messages.slack_register import get_slack_function
from slack_messages import app_settings as settings


class SlackAuthentication(BaseAuthentication):

    def authenticate(self, request):
        msg_data = request.data
        if msg_data.get('token') != settings.SLACK_VERIFICATION_TOKEN:
            raise exceptions.AuthenticationFailed('Incorrect auth token.')   


class DRSEventView(APIView):

    authentication_classes = [SlackAuthentication]

    def post(self, request, *args, **kwargs):
        if request.data.get('type') == 'url_verification':
            challenge = request.data.get('challenge')       
            return Response(data=challenge, status=status.HTTP_200_OK)
        event = request.data.get('event')
        if func:
                func(request.data)
        return Response(status=status.HTTP_200_OK)


class DRSCommandView(APIView):

    authentication_classes = [SlackAuthentication]

    def post(self, request, *args, **kwargs):
        command = request.data['command'].replace('/', '')
        func = get_slack_function(command)
        if not func:
            return Response(status=status.HTTP_404_NOT_FOUND)
        res = func(request.data)
        return Response(res, status=status.HTTP_200_OK)