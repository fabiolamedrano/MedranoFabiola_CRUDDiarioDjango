from django.shortcuts import render
from .models import *
from .forms import DiaryEntries, UserProfileForm
from django.urls import reverse_lazy

#GENERICS CREATEVIEW
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


class CreateProfile(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('diario_list')
    template_name = "form_createuser.html"

class CreateDiaryEntry(CreateView):
    model = DiarioMiki
    form_class = DiaryEntries
    success_url = reverse_lazy('diario_list')
    template_name = "form_creatediary.html"

class DiarioListView(ListView):
    model = DiarioMiki
    template_name = "diario_list.html"
    context_object_name = "entradas"

    def get_queryset(self):
        return DiarioMiki.objects.filter(user=self.request.user)

class DiarioDetailView(DetailView):
    model = DiarioMiki
    template_name = "diario_detail.html"
    context_object_name = "entrada"

    def get_queryset(self):
        return DiarioMiki.objects.filter(user=self.request.user)

class DiarioUpdateView(UpdateView):
    model = DiarioMiki
    form_class = DiaryEntries
    template_name = "diario_form.html"
    success_url = reverse_lazy('diario_list')

    def get_queryset(self):
        return DiarioMiki.objects.filter(user=self.request.user)

class DiarioDeleteView(DeleteView):
    model = DiarioMiki
    template_name = "diario_confirm_delete.html"
    success_url = reverse_lazy('diario_list')

    def get_queryset(self):
        return DiarioMiki.objects.filter(user=self.request.user)