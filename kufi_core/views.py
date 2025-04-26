from django.shortcuts import render

def home_kufi(request):
    return render(request, 'kufi_core/home_kufi.html')