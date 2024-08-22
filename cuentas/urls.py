from django.urls import path
from .views import vista_login, vista_logout

urlpatterns =[
    path('login', vista_login, name='login'),
    path('logout', vista_logout, name='logout')
]