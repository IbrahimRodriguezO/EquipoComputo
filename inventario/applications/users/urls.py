from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path(
        "register/",
        views.UserRegisterView.as_view(),
        name= "user-register"
    ),
    path(
        "",
        views.LoginUser.as_view(),
        name= "user-login"
    ),
    path(
        "logout/",
        views.LogoutUser.as_view(),
        name= "user-logout"
    ),
    path(
        "lista-user/",
        views.ListaUsers.as_view(),
        name= "lista-user"
    ),
    path(
        "update-user/<pk>",
        views.UpdateUser.as_view(),
        name= "update-user"
    ),
    path(
        'delete-user/<pk>/', 
        views.DeleteUser.as_view(),
        name='delete-user',
    ),  
]