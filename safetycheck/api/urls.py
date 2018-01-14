from django.conf.urls import url
from .views import CreateUserView
from rest_framework.authtoken import views
from.views import *

urlpatterns = [
    url(r'^register/', CreateUserView.as_view(), name='account-create'),
    url(r'^login/', login.as_view(), name='login'),
    url(r'^user_bac/', user_bac_view.as_view(), name='login'),


    ]