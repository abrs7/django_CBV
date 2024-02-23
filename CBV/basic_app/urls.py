from django.urls import path, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(), name='school_list'),
    # path('(?p<pk>[-\w]+/$)',views.SchoolDetailView.as_view(), name='school_detail'),
    # path('basic_app/(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='school_detail'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='school_detail'),
    re_path('basic_app/create/$', views.SchoolCreateView.as_view(), name='create'),
    path('basic_app/school_update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('basic_app/school_list',views.SchoolListView.as_view(), name='school_list'),
    # path('basic_app/create/$', views.SchoolCreateView.as_view(), name='create'),
    

]