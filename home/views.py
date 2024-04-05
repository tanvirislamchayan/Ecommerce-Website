from django.shortcuts import render

# Create your views here.

def home(request):
    page = 'Home | Django'
    context = {
        'page': page,
    }
    return render(request, 'home/home.html', context)


def contact(request):
    page = 'Contact Us | Django'
    context = {
        'page': page,
    }
    return render(request, 'contact/contact.html', context)


def about(request):
    page = 'About Us | Django'
    context = {
        'page': page,
    }
    return render(request, 'contact/about.html', context)



def blog(request):
    page = 'Blog | Django'
    context = {
        'page': page
    }
    return render(request, 'home/blog.html', context)



def services(request):
    page = 'Services | Django'
    context = {
        'page': page,
    }
    return render(request, 'contact/contact.html', context)

