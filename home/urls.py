from django.urls import path
from home import views
from home.views import RegisterView, LoginView, LogoutView, UserView

urlpatterns = [
    path('', views.index, name='home'),
    path('employee', views.employeeApi),
    path('employee/<id>',views.employeeApi),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]