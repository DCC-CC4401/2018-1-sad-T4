from django.shortcuts import render

# Create your views here.

def landing_user(request):

    return render(request, 'usersApp/landing_user.html')