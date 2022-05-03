from django.urls import path,include
from first_app import views

#TEMPLATE TAGGING

app_name = 'first_app'

urlpatterns =[
    path('',views.index,name='index'),
    path('help/',views.help,name='help'),
    path('users/',views.users,name='users'),
    path('relative/',views.relative,name='relavite'),
    path('other/',views.other,name='other'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
