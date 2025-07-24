from django.shortcuts import render

def landingPage(request):
  return render(request, 'landing.html')  


def profilePage(request):
  return render(request, "profile.html")