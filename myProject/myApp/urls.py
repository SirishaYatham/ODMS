from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.register, name='register'),
    path('user_home/', views.user_home, name='user_home'),
    path('login/', views.login_view, name='login_view'),
    path('login/admin_home/login.html', views.logout_view, name='logout_view'),  
    path('register/user/', views.register_user, name='register_user'),
    path('register/admin/', views.register_admin, name='register_admin'),
    path('login/user_home/', views.user_home, name='user_home'),
    path('login/admin_home/',views.admin_home, name = 'admin_home'),
    path('submit_organ_donation/', views.submit_organ_donation, name='submit_organ_donation'),
    path('get_donors/', views.get_donors, name='get_donors'),  # Add this line
    path('login/admin_home/new_organ_donation.html',views.submit_organ_donation,name = "submit_organ_donation"),
    path('new_organ_donation/', views.new_organ_donation, name='new_organ_donation'),
    path('delete_donor/<int:donor_id>/', views.delete_donor, name='delete_donor'),
    path('edit_organ_donation/<int:donor_id>/', views.edit_organ_donation, name='edit_organ_donation'),  # Add this line
    path('donated_organs/', views.donated_organs, name='donated_organs'),  # New URL pattern
    path('receiver_details/<int:donor_id>/', views.receiver_details, name='receiver_details'),
    
]
