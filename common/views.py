from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request,'common/index.html')

def about_us_view(request):
    return render(request,'common/about_us.html')

def course_view(request):
    return render(request,'common/course.html')

def notice_view(request):
    return render(request,'common/notice.html')

def contact_us_view(request):
    return render(request,'common/contact_us.html')