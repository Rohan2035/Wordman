from django.urls import path
from keeper import views

urlpatterns = [

    path('', views.index.as_view(), name='keeper-index'),
    path('generate-key/', views.get_key.as_view(), name='keeper-get-key'),
    path('add-password/', views.add_password.as_view(), name='keeper-add-password'),
    path('view-password/', views.view_password.as_view(), name='keeper-view-password'),
    path('delete-password/', views.delete_password, name='keeper-delete-password'),

]