from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from cryptography.fernet import Fernet
from keeper import models 
from keeper.forms import addPasswordForms
from django.contrib.auth.decorators import login_required


# Index Page
class index(LoginRequiredMixin, View):

    template_name = 'keeper/index-1.html'
    profiles = models.profile

    def get(self, request):

        flag = True

        if self.profiles.objects.filter(user_profile = request.user).exists():

            flag = False
            

        context = {'flag' : flag}
        return render(request, self.template_name, context)

# Key Generation 
class get_key(LoginRequiredMixin, View):

    template_name = 'keeper/generate-key.html'
    profiles = models.profile

    def get(self, request):

        # Updating User Profile
        profile_obj = self.profiles(user_profile = request.user, key = True)
        profile_obj.save()

        # Key Generation 
        key = Fernet.generate_key()

        context = {'key' : key.decode()}

        return render(request, self.template_name, context)

# Adding Password  
class add_password(LoginRequiredMixin, View):

    template_name = 'keeper/add.html'
    invalid_msg = 'Please Enter a Valid Key 🔑🔑'
    store = models.password_store

    def encrypt_func(self, key, password):
        
        try:
            
            ec_handler = Fernet(key)
            enc_password = ec_handler.encrypt(password)
            enc_password = enc_password.decode()
        
        except:

            return self.invalid_msg

        return enc_password
    
    def get(self, request):

        form = addPasswordForms()

        return render(request, self.template_name, {'form' : form})

    def post(self, request):

        form = addPasswordForms(request.POST)

        if form.is_valid():

            password_label = form.cleaned_data['password_label']
            key = form.cleaned_data['key'].encode()
            password = form.cleaned_data['password'].encode()

            # Check whether the object exists
            if self.store.objects.filter(password_label = password_label, user_profile = request.user).exists():

                messages.warning(request, 'The password already exists ⚠⚠')
                return redirect('keeper-add-password')


            # Save the form temporarily 
            form_post = form.save(commit=False)

            # Attach the user who adds the password
            form_post.user_profile = request.user

            enc_password = self.encrypt_func(key, password)

            # Check for the Key
            if enc_password == self.invalid_msg:

                messages.warning(request, self.invalid_msg)

            else:

                # Updating Forms
                form_post.password = enc_password
                form_post.save()

                # Success Message
                messages.info(request, 'Password Added Successfully 👍👍')
        
        return redirect('keeper-add-password')

# Viewing the Stored password
class view_password(LoginRequiredMixin, View):

    template_1 = 'keeper/view-password-2.html'
    store = models.password_store

    def decryption_func(self, key, password):
        
        try:
            
            dec_handler = Fernet(key)
            dec_password = dec_handler.decrypt(password)
        
        except:

            return "Invalid Key"

        return dec_password.decode()

    def get(self, request):

        store_handler = self.store.objects.filter(user_profile = request.user)
        context = {'profiles': store_handler}

        return render(request, self.template_1, context)

    def post(self, request):

        password_label = request.POST['password_label']
        key = request.POST['key'].encode()

        # Fetching the password
        store_handler = self.store.objects.get(password_label = password_label)
        password = store_handler.password.encode()

        dec_password = self.decryption_func(key, password)

        context = {'label' : password_label, 'password' : dec_password}
        return render(request, self.template_1, context)

# Deleting Passwords
@login_required
def delete_password(request):

    if request.method == 'POST':
        
        password_id = request.POST['id']
        store_handler = models.password_store.objects.get(id = password_id)
        store_handler.delete()

        return redirect('keeper-view-password')



    
        
        
        
