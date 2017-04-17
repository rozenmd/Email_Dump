from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

from web.models import Email


# @csrf_exempt
def on_incoming_message(request, key=None):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject', '')

        body_plain = request.POST.get('body-plain', '')
        body_without_quotes = request.POST.get('stripped-text', '')
        # note: other MIME headers are also posted here...
        Email(sender=sender, recipient=recipient, subject=subject,
              body_plain=body_plain, body_without_quotes=body_without_quotes).save()
        # attachments:
        # for key in request.FILES:
        #     file = request.FILES[key]
            # do something with the file

    # Returned text is ignored but HTTP status code matters:
    # Mailgun wants to see 2xx, otherwise it will make another attempt in 5 minutes
    return HttpResponse('OK')
