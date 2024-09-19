# accounts/views.py

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import UserProfile, AdminRegister
from datetime import date
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache
from django.http import HttpResponse


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def landing_page(request):
    return render(request, 'myApp/landingPage.html')

def register(request):
    return render(request, 'myApp/register_role.html')

@never_cache
@login_required
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def user_home(request):
    context = {
        'username': request.user.first_name  # Pass the username to the template
    }
    return render(request, 'myApp/user_home.html', context)
@never_cache
@login_required
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def admin_home(request):
    context = {
        'username': request.user.email  # Pass the username to the template
    }
    return render(request, 'myApp/admin_home.html', context)

def authenticate_user(email, password):
    try:
        # Check if the email exists in UserProfile
        user_profile = UserProfile.objects.get(mailId=email)
        # Check if the password matches
        if user_profile.password == password:
            return user_profile
    except UserProfile.DoesNotExist:
        pass

    return None

def authenticate_admin(email, password):
    try:
        # Check if the email exists in AdminRegister
        admin = AdminRegister.objects.get(email=email)
        # Check if the password matches
        if admin.password == password:
            return admin
    except AdminRegister.DoesNotExist:
        pass

    return None

from django.http import JsonResponse

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        login_type = request.POST.get('loginType')  # Get the login type
        print(f"Email: {email}, Password: {password}, Login Type: {login_type}")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if login_type == 'user':
                return JsonResponse({'success': True, 'redirect_url': reverse('user_home')})  # Redirect to user home
            elif login_type == 'admin':
                return JsonResponse({'success': True, 'redirect_url': reverse('admin_home')})  # Redirect to landing page
        else:
            return JsonResponse({'success': False, 'error': 'Invalid email or password.'})

    return render(request, 'myApp/login.html')

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    response = redirect('login_view')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Expires'] = '0'
    response['Pragma'] = 'no-cache'
    return response


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def register_user(request):
    if request.method == 'POST':
        print("Form submitted")
        print(request.POST)

        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        phone_number = request.POST.get('phNum')
        date_of_birth = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = request.POST.get('mailId')
        country = request.POST.get('country')
        address = request.POST.get('address')
        password = request.POST.get('registerInputUser')
        password_confirm = request.POST.get('registerInputUserRecheck')
        #hashed_password = make_password(password)

        
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('register_user')
        
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register_user')
         # Check if phone number is already registered
        if UserProfile.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Phone number is already registered.")
            return render(request, 'myApp/register_user.html')

        # Check if phone number is 10 digits
        if len(phone_number) != 10:
            messages.error(request, "Phone number must be 10 digits.")
            return render(request, 'myApp/register_user.html')

        # Check if age is above 18
        dob = date.fromisoformat(date_of_birth)
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            messages.error(request, "You must be at least 18 years old to register.")
            return render(request, 'myApp/register_user.html')
        
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        
        user_profile = UserProfile.objects.create(
            user=user,
            firstName=first_name,
            lastName=last_name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            gender=gender,
            mailId=email,
            country=country,
            address=address,
            password=password
        )
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')
        else:
            messages.error(request, "Authentication failed.")
            return redirect('register_user')

    return render(request, 'myApp/register_user.html')


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def register_admin(request):
    if request.method == 'POST':
        # Extract form data
        admin_code = request.POST.get('adminCode')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        phone_number = request.POST.get('phNum')
        date_of_birth = request.POST.get('dob')
        designation = request.POST.get('designation')
        gender = request.POST.get('gender')
        email = request.POST.get('mailId')
        country = request.POST.get('country')
        address = request.POST.get('address')
        password = request.POST.get('registerInputAdmin')
        password_confirm = request.POST.get('registerInputAdminRecheck')
        #hashed_password = make_password(password)

        developer_code = 'SirishaDev@'  # Replace this with your actual developer code

        # Check developer code
        if admin_code != developer_code:
            messages.error(request, "Invalid developer code.", extra_tags='register')
            return redirect('register_admin')

        # Check for password match
        if password != password_confirm:
            messages.error(request, "Passwords do not match.", extra_tags='register')
            return redirect('register_admin')

        # Check if email already exists
        if AdminRegister.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.", extra_tags='register')
            return redirect('register_admin')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Create admin
        AdminRegister.objects.create(
            admin_code=admin_code,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            designation=designation,
            gender=gender,
            email=email,
            country=country,
            address=address,
            password=password
        )
        
        return redirect('login_view')

    return render(request, 'myApp/register_admin.html')


# myApp/views.py
from .models import OrganDonor

# Other views...
@login_required
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def new_organ_donation(request):
    return render(request, 'myApp/new_organ_donation.html')

from django.urls import reverse

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
@login_required
def submit_organ_donation(request):
    if request.method == 'POST':
        name = request.POST.get('donorname')
        location = request.POST.get('location')
        organ = request.POST.get('organ')
        age = request.POST.get('age')
        phone_number = request.POST.get('contact')
        hospital = request.POST.get('hospital')
        blood_group = request.POST.get('bloodGroup')

        # Create a new OrganDonor entry
        OrganDonor.objects.create(
            donorname=name,
            location=location,
            organ=organ,
            age=age,
            contact=phone_number,
            hospital=hospital,
            bloodgroup=blood_group,
            flag=False  # Default flag value for new entries
        )

        redirect_url = reverse('admin_home')
        return JsonResponse({'success': True, 'redirect_url': redirect_url})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})


@login_required
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def delete_donor(request, donor_id):
    if request.method == 'POST':
        try:
            donor = OrganDonor.objects.get(id=donor_id)
            receiver_name = request.POST.get('receiver_name')
            receiver_contact = request.POST.get('receiver_contact')
            receiver_location = request.POST.get('receiver_location')

            donor.flag = True
            donor.receiver_name = receiver_name
            donor.receiver_contact = receiver_contact
            donor.receiver_location = receiver_location
            donor.save()
            return JsonResponse({'success': True})
        except OrganDonor.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Donor not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def get_donors(request):
    organ_name = request.GET.get('organ')
    donors = OrganDonor.objects.filter(organ__icontains=organ_name, flag=False)
    donor_list = list(donors.values())
    return JsonResponse(donor_list, safe=False) 

@login_required
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def edit_organ_donation(request, donor_id):
    donor = get_object_or_404(OrganDonor, id=donor_id)
    if request.method == 'POST':
        donor.donorname = request.POST.get('donorname')
        donor.location = request.POST.get('location')
        donor.organ = request.POST.get('organ')
        donor.age = request.POST.get('age')
        donor.contact = request.POST.get('contact')
        donor.hospital = request.POST.get('hospital')
        donor.bloodgroup = request.POST.get('bloodGroup')
        donor.save()
        redirect_url = reverse('admin_home')
        return JsonResponse({'success': True, 'redirect_url': redirect_url})
    
    context = {
        'donor': donor
    }
    return render(request, 'myApp/new_organ_donation.html', context)

@login_required
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def donated_organs(request):
    donors = OrganDonor.objects.filter(flag=True)
    context = {'donors': donors}
    return render(request, 'myApp/donated_organs.html', context)

@login_required
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def receiver_details(request, donor_id):
    donor = get_object_or_404(OrganDonor, id=donor_id)
    
    if request.method == 'POST':
        receiver_name = request.POST.get('receiver_name')
        receiver_contact = request.POST.get('receiver_contact')
        receiver_location = request.POST.get('receiver_location')
        
        donor.receiver_name = receiver_name
        donor.receiver_contact = receiver_contact
        donor.receiver_location = receiver_location
        donor.flag = True
        donor.save()
        
        return redirect('admin_home')
    
    context = {
        'donor': donor
    }
    return render(request, 'myApp/receiver_details.html', context)
