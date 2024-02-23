from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.


def index(request):
    contex = {
        'variable': "This data is sent from Views file"
    }
    messages.success(request, 'THis is the test messeges')
    return render(request, "index.html", contex)


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact = Contact(name=name, email=email, desc=desc, date=date)
        contact.save()
        messages.success(request, "Your messege has been sent.")
    return render(request, "contact.html")


'''
$ python manage.py shell
Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from home.models import Contact
>>> contact.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'contact' is not defined
>>> Contact.objects.all() 
<QuerySet [<Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>]>
>>> Contact.objects.all()[0]
<Contact: Black 2.o>
>>> Contact.objects.all()[0].name
'Black 2.o'
>>> Contact.objects.all()[0].email
'noob125690@gmail.com'
>>> Contact.objects.all()[0].desc 
'Hello Black, How ARe You?'
>>> Contact.objects.filter(name="Black 2.o")
<QuerySet [<Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>, <Contact: Black 2.o>]>
>>> ins = Contact.objects.filter(name="Black 2.o")[0] 
>>> ins.name = "Yousuf" 
>>> ins.save()
>>>  
'''
