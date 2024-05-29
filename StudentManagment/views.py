from django.shortcuts import render,redirect
from Login_Logout.models import User, Profile
from django.contrib.auth.decorators import login_required

@login_required
def User_data(request):
    
    userData = User.objects.filter(user=request.user)
    
      
    return render(request,'base.html', { 'UserData': userData })

