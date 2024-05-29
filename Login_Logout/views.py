from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from .models import User, Sponsor, Profile
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from .utils import generate_refferal_link
from django.conf import settings

User = get_user_model() 



# এখানে আমি একজন ইউজার রেজিস্টার করার জন্য ভিউস এর কোড করসি 


def Register(request):
    profile_id = request.session.get('ref_profile')
    form = RegisterForm(request.POST or None)
    recommended_by_profile = None  # Initialize the variable here

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            
            if profile_id is not None:
                try:
                    recommended_by_profile = Sponsor.objects.get(id=profile_id)
                except Sponsor.DoesNotExist:
                    recommended_by_profile = None

            registered_profile = Sponsor.objects.get(user=user)
            if recommended_by_profile:
                registered_profile.recommended_by = recommended_by_profile.user
                registered_profile.save()
            
            messages.success(request, 'Account registered successfully')
            return redirect('Registerpage')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    
    return render(request, 'register.html', {'form': form})



# এখানে আমি Refferal Code Generate  কোড করসি

def Refferal_code_generate(request, *args, **kwargs):
    
    code = str(kwargs.get('ref_code'))
    
    
    try:
        profile = Sponsor.objects.get(code = code)
        request.session['ref_profile'] = profile.id
        print('id', profile.id)
        
    except:
        pass
    
    print(request.session.get_expiry_date())
    
    
    refferal_link = generate_refferal_link(request)
    print('hello')
        
    return render(request,'refferal.html', )




# এখানে আমি একজন ইউজার login করার জন্য ভিউস এর কোড করসি

def LoginView(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(email = email, password = password)
            
            if user is not None:
                login(request,user)
                messages.success(request, f' welcome {user.first_name} {user.last_name} !!')
                return redirect('homepage')
            
            else:
                messages.success(request,'Loggin info incorrect')
                
    else:
        form = AuthenticationForm()
        
    return render(request,'login.html', {'form':form} )


# এখানে আমি একজন ইউজার Logout করার জন্য ভিউস এর কোড করসি


@login_required
def LogoutView(request):
    user = request.user
    logout(request)
    messages.success(request, f'{user.first_name} {user.last_name} is successfully logged out.')
    return redirect('loginpage')
 


# এখানে আমি একজন ইউজার এর profile এর  কোড করসি

def view_Student_Profile(request):
    return render(request,'profile.html')




def ReffaralLinkView(request):
    print('hello world')
    print(request.user)
    # refferal_link = generate_refferal_link(request)
    # print(request.user.user.code)
    base_url = settings.BASE_URL
    
    user_sponsor = request.user.sponsor
    refferal_code = user_sponsor.code
    print(request.user)
    
    refferal_link = f"{base_url}/Login_Logout/Register/?ref_code={refferal_code}"
    print(refferal_link)
    
    return render(request, 'refferal.html', {'refferal_link': refferal_link})