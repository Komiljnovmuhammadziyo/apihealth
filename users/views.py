from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from users.forms import RegisterForm, UpdateProfileForm


class UserCreateViews(View):
    def get(self,request):
        register_form = RegisterForm
        messages.info(request,'You have an account now you need login')
        context = {
            'form':register_form
        }

        return render(request, template_name='registration/register.html', context=context)
    def post(self, request):

        create_form = RegisterForm(data= request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('user:login_page' )
        else:
            context = {
                'form':create_form
            }
            return render(request, template_name='registration/register.html', context=context)
#

class LoginUserView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        # user = request.user
        # user_se_key = request.COOKIES.get('sessionid')
        # print(user.is_authenticated)
        # print(user_se_key)
        context = {
            'form': login_form
        }

        return render(request, template_name='login.html', context=context)
    def post(self, request):

        login_form = AuthenticationForm(data= request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You have been Log In now')
            return redirect('home_page')

        else:
            return render(request, template_name='login.html', context={'form':login_form})

class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'registration/profile.html',{'user': request.user})



class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request,'You have been logged out')
        return redirect('user:login_page')

class UpdateProfileView(LoginRequiredMixin, View):
    def get(self, request):
        userform = UpdateProfileForm(instance=request.user)

        return render(request, 'registration/profile_update.html', {'form': userform})

    def post(self, request):
        user = UpdateProfileForm(instance=request.user,
                                 data=request.POST,
                                 files=request.FILES
                                 )

        if user.is_valid():
            user.save()
            messages.success(request,'Your updates is save !')
            return redirect('user:profile')
        return render(request,'registration/profile_update.html', {'form':user})
