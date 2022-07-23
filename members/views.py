from django.contrib import messages
from django.shortcuts import render, redirect
from members.forms import registration_forms

# Create your views here.

def register(request):
    
    if request.method == 'POST':

        register_form = registration_forms(request.POST)

        if register_form.is_valid():

            register_form.save()
            messages.success(request, 'Account Sucessfully Created')
            return redirect('login')

    else:

        register_form = registration_forms()

    context = {'form' : register_form}

    return render(request, 'members/register.html', context)
