from django.shortcuts import render

# Welcome page
def welcome_page(request):
    return render(request,'renters/welcome_page.html')
