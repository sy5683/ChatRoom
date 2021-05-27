from django.shortcuts import render


# Create your views here.

def not_found_404(request, exception):
    return render(request, 'error/404.html')


def not_found(request):
    return render(request, 'error/404.html')


def server_error_500(request):
    return render(request, 'error/500.html')


def server_error(request):
    return render(request, 'error/500.html')
