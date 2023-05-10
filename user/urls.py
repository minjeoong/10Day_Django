from django.urls import path
from .views import signin,signup,signout, new_profile, create_profile


app_name = 'user'

urlpatterns = [
    path("signin/", signin, name='signin'),
    path("signup/", signup, name='signup'),
    path("signout/", signout , name='signout'),
    path('new_profile/', new_profile, name='new_profile'),
    path('create_profile/', create_profile, name='create_profile'),
]
