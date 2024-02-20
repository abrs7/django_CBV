from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(), name='school_list'),
    # path('(?p<pk>[-\w]+/$)',views.SchoolDetailView.as_view(), name='school_detail'),
    path('basic_app/(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='school_detail'),

]