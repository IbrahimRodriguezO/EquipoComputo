from django.shortcuts import render
# IMPORTACIONES NECESARIAS
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.views.generic import ListView, UpdateView, DeleteView
from .models import User
from .forms import UserRegisterForm, UpdateUser
from django.urls import reverse, reverse_lazy
from .forms import UserRegisterForm

# Create your views here.
class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users_app:lista-user")

    def form_valid(self, form):
        usuario = User.objects.create_user(
            form.cleaned_data["username"],
            form.cleaned_data["email"],
            form.cleaned_data["role"],
            form.cleaned_data["password1"],
            nombres=form.cleaned_data["nombres"],
            apellidos=form.cleaned_data["apellidos"]
        )
        return super(UserRegisterView, self).form_valid(form)
    

class LoginUser(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("inventario_app:add-inventario")
    
    def form_invalid(self, form):
        messages.error(self.request, "Usuario o contraseña incorrectos")
        return super().form_invalid(form)
    
    
class LogoutUser(LogoutView):
    next_page = reverse_lazy("users_app:user-login")


class ListaUsers(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/user-list.html"
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(ListaUsers, self).get_context_data(**kwargs)
        context["usuarios"] = User.objects.all().order_by("-id")
        return context
    

class UpdateUser(FormView):
    form_class = UpdateUser
    template_name = "users/update-user.html" 
    success_url = reverse_lazy("users_app:lista-user")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user_id = self.kwargs["pk"]
        kwargs["instance"] = User.objects.get(pk=user_id)
        return kwargs
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(UpdateUser, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        context["usuario"] = User.objects.get(id=pk)
        return context
    

class DeleteUser(DeleteView):
    model = User
    success_url = "."

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(
            reverse(
                "users_app:lista-user",
            )
        )
