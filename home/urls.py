from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('employee', views.employeeApi),
    path('employee/<id>',views.employeeApi)
]