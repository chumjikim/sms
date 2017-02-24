from django.shortcuts import render

from sms.forms import SMSForm


def send_message_write(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
    else:
        form = SMSForm(
        )
    context = {
        'form': form,
    }
    return render(request, 'sms/sms-send.html', context)
