# from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from . import models
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['Inject_me'] = 'Bro you are doing it well!!'
        return context

class SchoolListView(ListView):
    context_object_name = 'school_list'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name  = 'basic_app/school_detail.html'    
class SchoolCreateView(CreateView):
    # context_object_name = 'create'
    fields = ('name', 'principal', 'location' )
    model = models.School
    
class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal', 'location' )

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:school_list')