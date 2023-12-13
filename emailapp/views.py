from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import UserProfile1
from .utils import generate_username, generate_password
from django.core.mail import send_mail
from django.conf import settings

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        # Generate username and password
        username = generate_username(name)
        password = generate_password()

        # Create the user
        hashed_password = make_password(password)
        user = UserProfile1(name=name, email=email, username=username, password=hashed_password)
        user.save()

        # Send email with username and password
        subject = 'Account Registration'
        message = f'Hello {name},\n\nYour account has been created.\n\nUsername: {username}\nPassword: {password}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a success page or perform additional actions
        return redirect('signup')

    return render(request, 'emailapp/signup.html')
def display_table(request):
    # Fetch all rows from the database table
    rows = UserProfile1.objects.all()

    # Pass the rows to the template for rendering
    return render(request, 'emailapp/display_table.html', {'rows': rows})