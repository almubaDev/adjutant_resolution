from django.shortcuts import render

def diagrama_kufi_view(request):
    return render(request, 'tecnical_support/diagrama_kufi.html')