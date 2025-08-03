from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def howitworks(request):
    return render(request, 'howitworks.html')

def blog(request):
    return render(request, 'blog.html')

def blog1(request):
    return render(request, 'blog1.html')

def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request, 'blog3.html')

def locations(request):
    return render(request, 'locations.html')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')

def contact(request):
    return render(request, 'contact.html')