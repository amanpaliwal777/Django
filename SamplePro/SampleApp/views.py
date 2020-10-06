from django.shortcuts import render
from .models import Contact, Feedback, Enquiry
from .feedform import FeedForm
from django.http import HttpResponse


def home(request):
    return render(request, 'Home.html')


def enquiry(request):
    if request.method == 'POST':
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        email1 = request.POST.get('email')
        mobile1 = request.POST.get('mobile')

        def cou():
            if request.POST['course']:
                return ','.join(request.POST.getlist('course'))

        def lou():
            if request.POST['location']:
                return ','.join(request.POST.getlist('location'))

        course1 = list(cou().split(sep=','))
        location1 = list(lou().split(sep=','))

        data = Enquiry(
            first_name=fname1,
            last_name=lname1,
            email = email1,
            mobile=mobile1,
            course=course1,
            location=location1
        )
        data.save()
        return render(request, 'Enquiry.html')

    else:
        return render(request, 'Enquiry.html')


def services(request):
    return render(request, 'services.html')


def feedback(request):
    if request.method == 'POST':
        fform = FeedForm(request.POST)
        if fform.is_valid():
            name1 = request.POST.get('name')
            rating1 = request.POST.get('rating')
            feedback1 = request.POST.get('feedback')
            data = Feedback(
                name=name1,
                rating=rating1,
                feedback=feedback1
            )
            data.save()
            a = Feedback.objects.all()
            fform = FeedForm()
            return render(request, 'feedback.html', {'fform': fform, 'data': a})
        else:
            return HttpResponse('Invalid form')
    else:
        fform = FeedForm()
        a = Feedback.objects.all()
        return render(request, 'feedback.html', {'fform': fform, 'data': a})


def gallery(request):
    return render(request, 'photos.html')
