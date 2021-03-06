# coding: utf-8
import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import mail_admins

from .models import Blacklist


@csrf_exempt
def sns_notification(request):
    """
    Receive AWS SES bounce SNS notification
    """

    # decode json
    try:
        data = json.loads(request.read())
    except ValueError:
        return HttpResponseBadRequest('Invalid JSON')

    # handle SNS subscription
    if data['Type'] == 'SubscriptionConfirmation':
        subscribe_url = data['SubscribeURL']
        subscribe_body = """
        Please visit this URL below to confirm your subscription with SNS

        %s """ % subscribe_url

        mail_admins('Please confirm SNS subscription', subscribe_body)
        return HttpResponse('OK')

    #
    try:
        message = json.loads(data['Message'])
    except ValueError:
        assert False, data['Message']

    #
    type = 0 if message['notificationType'] == 'Bounce' else 1
    email = message['mail']['destination'][0]


    # add email to blacklist
    try:
        Blacklist.objects.get(email=email)
    except Blacklist.DoesNotExist:
        Blacklist.objects.create(email=email, type=type)

    return HttpResponse('Done')
