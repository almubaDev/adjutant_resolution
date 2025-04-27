from django.shortcuts import render, redirect


def dashboard_diary(request):
    return render(request, 'diary_assistant/dashboard_diary.html')