from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import (
  authenticate,
  get_user_model,
  login,
  logout,
)
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from blog.models import Post,PostDetail
from Erudite import settings as sett


# Create your views here.

class UserFormView(View):
    form_class = UserForm
    template_name = 'users/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password =  form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('blog:index')

        return render(request, self.template_name, {'form':form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                queryset = PostDetail.objects.all()
                context = {
                    'object_list':queryset
                }
                return render(request, 'blog/index.html', context)
            else:
                return render(request, 'users/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'users/login.html', {'error_message': 'Invalid login'})

    return render(request, 'users/login.html', {'error_message': ''})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'users/login.html', context)