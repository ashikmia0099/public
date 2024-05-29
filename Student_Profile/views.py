from django.shortcuts import render,redirect
from Login_Logout.models import User, Profile
from .models import Student_image,Student_Certificate
from django. views import View
from Login_Logout.forms import RegisterForm,User_Update_Form  
from .forms import Student_Info_Forms  
from django.contrib.auth.decorators import login_required


def Student_info(request):
    
    if request.method == 'POST':
        form = Student_Info_Forms(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            
    else:
        form = Student_Info_Forms(instance = request.user)
        
        image = Student_image.objects.filter(user=request.user).last()

    
    return render(request, 'student_info.html',{'form':form, 'user':image})


   




def ChangeInfo(request):
    if request.method == 'POST':
        form = User_Update_Form(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('student_dataUpdate')
    else:
        form = User_Update_Form(instance=request.user)
        
        
    # change student image 
    
    image = Student_image.objects.filter(user=request.user).last()
    
    return render(request, 'update_info.html', {'form': form , 'user':image})




def Student_Certificate_view(request):
    user = request.user

    try:
        pdf = Student_Certificate.objects.get(user=user)
    except Student_Certificate.DoesNotExist:
        pdf = None

    return render(request, 'certificate.html', {'pdf': pdf})
    
