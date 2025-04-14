from django.urls import path

from aminapi import views

urlpatterns = [

    path('getcontact' ,views.GenericAPIView.as_view() ),
    path('createcontact' , views.GenericCreateAPIView.as_view() ),
    path('login' , views.LoginAPIView.as_view() ),

]