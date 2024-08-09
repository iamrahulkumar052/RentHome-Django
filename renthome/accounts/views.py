from django.shortcuts import render,redirect

# Sign In view
def sign_in(request):

    return render(request,'accounts/sign_in.html')

# Choose user type view
def user_type(request):
    
    return render(request,'accounts/choose_user_type.html')

# Sign Up view
def sign_up(request):
    
    return render(request,'accounts/sign_up.html')