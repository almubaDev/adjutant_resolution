from django.shortcuts import render


def home_view(request):
    return render(request, 'app/home.html')


def assistant_view(request):
    return render(request, 'app/assistant.html')
