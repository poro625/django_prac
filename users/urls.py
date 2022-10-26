from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    
    path('home/',views.home ,name='home'),
    path('signup/', views.signup ,name='signup'),
    path('login/',views.login ,name='login'),
    path('logout/',views.logout ,name='logout'), # 로그아웃
    path('delte/',views.delte ,name='delte'), #회원탈퇴
    path('password/<int:id>/',views.password ,name='password'), # 비밀번호 변경 
    path('detail/<int:id>/',views.detail ,name='detail'), # 회원정보 변경

    
]
