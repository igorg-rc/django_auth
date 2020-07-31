from django.shortcuts import render
from django.contrib.auth.models import User

def showthis(request):
    all_users= user.objects.all()
    context= {'allusers': all_users}    
    return render(request, 'index.html', context)

