from django.shortcuts import render,redirect
from myapp.models import Appointment
from myapp.models import Contact
# Create your views here.
def home(request):
     return render(request,'index.html')

def service(request):
    return render(request, 'service.html')

def starter(request):
    return render(request,'starter.html')

def about(request):
    return render(request,'about.html')

def doctors(request):
    return render(request,'doc.html')

def myservice(request):
    return render(request,'services.html')

def appointment(request):
    if request.method == 'POST':
        myappointments = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            datetime = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message']
        )
        myappointments.save()
        return redirect('/appointment')

    else:
        return render(request,'appointment.html')



def show(request):
    allappointments=Appointment.objects.all()
    return render(request, 'show.html',{'appointment':allappointments})


def delete(request, id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()

    return redirect('/show')

def contact(request):
    if request.method == 'POST':
        contact_us = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        contact_us.save()
        return redirect('/contact')

    else:
        return render(request, 'contact.html')


def detail(request):
    contact_us=Contact.objects.all()
    return render(request, 'details.html',{'contact':contact_us})


def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()

    return redirect('/details')
