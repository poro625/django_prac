from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    
    path('signup/', views.signup ,name='signup'),
    path('login/',views.login ,name='login'),
    path('home/',views.home ,name='home'),
    
]
