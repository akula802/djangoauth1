# Import the needfuls
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm



# Home page
def home(request):
    return render(request, 'auth/home.html', {})



# The about page
def about(request):
    return render(request, 'auth/about.html', {})



# User action: Change password
def change_password(request):
    if request.method == "POST":
        # someone filled out the change form and submitted it
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            # Save the form, updating the user in the database
            form.save()

            # Update the session hash to the user isn't logged out on form submit
            update_session_auth_hash(request, form.user)

            # Redirect to home page with a message, and we're done
            messages.success(request, ('Password updated, $5 I see you again in <1 week :-)'))
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    
    # Render the page and form either way
    context = {'form': form}
    return render(request, 'auth/change_password.html', context)



# User action: Login
def login_user(request):
    if request.method == "POST":

        # Build the 'user' object
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # See if the user object exists in the database
        if user is not None:
            login(request, user)
            messages.success(request, ('Welcome, {} :-)'.format(username)))
            return redirect('home')
        else:
            messages.success(request, ('Fuck off, ya nobody.'))
            return redirect('login')

    else:
        return render (request, 'auth/login.html', {})


# User action: Logout
def logout_user(request):
    logout(request)
    messages.success(request, ('You have logged out.'))
    return redirect('home')



# User action: Register
def register_user(request):
    if request.method == "POST":
        # someone filled out the form and submitted it
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the form, adding the user to the database
            form.save()

            # Construct the user object
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Log in the user
            user = authenticate(request, username=username, password=password)
            login(request, user)

            # Redirect to home page with a message, and we're done
            messages.success(request, ('Welcome to the show, {} :-)'.format(username)))
            return redirect('home')
    else:
        form = SignUpForm()
    
    # Render the page and form either way
    context = {'form': form}
    return render(request, 'auth/register.html', context)



def edit_profile(request):
    if request.method == "POST":
        # someone filled out the change form and submitted it
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            # Save the form, updating the user in the database
            form.save()

            # Construct the user object
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password1']

            # Log in the user
            #user = authenticate(request, username=username, password=password)
            #login(request, user)

            # Redirect to home page with a message, and we're done
            messages.success(request, ('Deets updated nicely :-)'))
            return redirect('edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
    
    # Render the page and form either way
    context = {'form': form}
    return render(request, 'auth/edit_profile.html', context)


