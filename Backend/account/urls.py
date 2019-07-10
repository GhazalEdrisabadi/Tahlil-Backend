from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('account/', FileUploadView.as_view(), name='account'),
    path('viewUsersListandDesign/', views.viewUsersListandDesign, name='viewUsersListandDesign')
]
