from django.urls import path,include
from basic_app import views

#Template tagging

app_name = 'basic_app'


urlpatterns = [
	path('',views.relative,name='relative'),
	path('',views.other,name='other'),
]