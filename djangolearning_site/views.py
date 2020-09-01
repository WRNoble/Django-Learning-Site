from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def course_list(request):
    return render(request, "course_list.html")