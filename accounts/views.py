from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView, UpdateView

from .forms import SignUpForm, LoginForm, UpdateForm
from .models import Users


def default_url(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('dashboard'))
    else:
        return redirect(reverse_lazy('login'))


@login_required()
def logout_user(request):
    logout(request=request)
    return redirect(reverse_lazy('default_url'))


class LoginUser(FormView):
    template_name = 'login.html'
    success_url = reverse_lazy('dashboard')
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['menu'] = 'login'
        return context

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
            return redirect(reverse_lazy('dashboard'))
        else:
            return render(self.request, 'login.html', {'fail': 'Invalid Username or password', 'form': form})


class SignUp(CreateView):
    model = Users
    form_class = SignUpForm
    template_name = 'create_account.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        super(SignUp, self).form_valid(form)
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        # print(user)
        login(self.request, user)
        return redirect(reverse_lazy('dashboard'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['menu'] = 'create'
        return context


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = Users
    form_class = UpdateForm
    template_name = 'update_profile.html'

    def get_success_url(self):
        return reverse_lazy('update_profile', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['menu'] = 'update_profile'
        return context


'''class SignUp(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(self.request, 'create_account.html', {'form': form})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.FILES)
        form = SignUpForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('dashboard'))
        else:
            return render(self.request, 'create_account.html', {'form': form})'''
