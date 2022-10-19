from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView, ListView, DeleteView
from django.utils.timezone import datetime

from .models import Storage
from .forms import StorageForm


# we need to specify the LoginRequiredMixin First before the Template View
class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['menu'] = 'dashboard'
        context['user'] = self.request.user
        return context


class CreateFile(LoginRequiredMixin, FormView):
    form_class = StorageForm
    template_name = 'create_files.html'

    def form_valid(self, form):
        user = self.request.user.username
        file_name = form.cleaned_data['file_name']
        description = form.cleaned_data['description']
        file = form.cleaned_data['file']
        storage = Storage.objects.create(user=user, file_name=file_name, description=description,
                                         access_time=datetime.now(), file=file)
        storage.save()
        return redirect(reverse_lazy('view_files'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['menu'] = 'create_files'
        context['user'] = self.request.user
        return context


class ViewFile(ListView):
    model = Storage
    context_object_name = 'files'
    template_name = 'view_files.html'

    def get_queryset(self):
        return Storage.objects.filter(user=self.request.user.username).order_by('access_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['menu'] = 'view_file'
        return context


class DeleteFile(LoginRequiredMixin, DeleteView):
    model = Storage
    template_name = 'delete_file.html'
    success_url = reverse_lazy('view_files')
    context_object_name = 'file'

    def get_queryset(self):
        return Storage.objects.filter(pk=self.kwargs['pk'])
