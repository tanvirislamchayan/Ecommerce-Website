from django.shortcuts import render

# Create your views here.
def login(request):
    page = 'Login | Django'
    context = {
        'page': page
    }
    return render(request, 'account/login.html', context)


def signup(request):
    page = 'Sign UP | Django'
    context = {
        'page': page
    }
    return render(request, 'account/login.html', context=context)