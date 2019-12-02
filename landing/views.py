# landing/views.py
from django.shortcuts import get_object_or_404, render, redirect
#from django.http import HttpResponse
from .models import Developer
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from mailjet_rest import Client
import os

def index(request):#, developer_id):
    developer = Developer.objects.all() #get_object_or_404(Developer, pk=developer_id)
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            your_subject = form.cleaned_data['your_subject'] # request.POST['subject']
            your_email = form.cleaned_data['your_email'] # request.POST['email']
            your_message = form.cleaned_data['your_message'] # request.POST['message']
            recipients = ['arotev@gmail.com', 'tevdiego@gmail.com']
            if cc_myself:
                recipients.append(sender)
            # try:
            #     send_mail(subject, message, from_email, recipients)
            #     # mail.send_mail(
            #     #     sender="arotev@gmail.com",
            #     #     to="Ariel Tevelev <arotev@gmail.com>",
            #     #     subject="Your account has been approved",
            #     #     body="""Dear Albert:
            #     #         Your example.com account has been approved.  You can now visit
            #     #         http://www.example.com/ and sign in using your Google Account to
            #     #         access new features.

            #     #         Please let us know if you have any questions.

            #     #         The example.com Team
            #     #         """)
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            # return redirect('success')

            api_key = os.environ['EMAIL_API_KEY']
            api_secret = os.environ['EMAIL_API_SECRET']
            mailjet = Client(auth=(api_key, api_secret), version='v3.1')
            data = {
            'Messages': [
                {
                "From": {
                    "Email": "email@tevstudio.com",
                    "Name": "TevStudio Mail"
                },
                "To": [
                    {
                    "Email": recipients,
                    "Name": your_name
                    }
                ],
                "Subject": your_subject,
                "TextPart": your_message,
                "HTMLPart": your_message+"<br><h3>This mail was sent to you from Tevstudio.com <br> please contact "+your_name+" at "+ your_email +" </h3>",
                "CustomID": " "
                }
            ]
            }
            result = mailjet.send.create(data=data)
            if (result.status_code==200):
                print(result.json())
                return redirect('success')
            





    return render(request, 'landing/index.html', {'developer': developer, 'form': form})
    #return HttpResponse("Hello, world. You're at the polls index.")

def successView(request):
    return HttpResponse('Success! Thank you for your message.')