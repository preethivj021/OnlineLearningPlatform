from django.shortcuts import render
from .models import CourseData,FeedbackData
# Create your views here.
def home(request):
    return render(request,'insapp/home.html')

def contact(request):
    return render(request,'insapp/contact.html')

def services(request):
    cd=CourseData.objects.all()
    return render(request,'insapp/services.html',{'cd':cd})

def feedback(request):
    if request.method=='GET':
        return render(request,'insapp/feedback.html')
    else:
        FeedbackData(
            name=request.POST.get('name'),
            rating=request.POST.get('rating'),
            comment=request.POST.get('comment')

        ).save()
        fd=FeedbackData.objects.all()
        return render(request,'insapp/feedback.html',{'fd':fd})

def gallery(request):
    return render(request,'insapp/gallery.html')
def view(request):
    return render(request,'insapp/gallery.html')
