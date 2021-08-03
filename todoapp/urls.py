from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# app_name="todoapp"

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('list', views.list.as_view(), name='list'),
    path('submit', views.submit.as_view(), name='submit'),
    path('delete/<int:pk>', views.delete.as_view(), name='delete'),
    path('sortdata', views.sortdata.as_view(), name='sortdata'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('searchdata', views.searchdata.as_view(), name='searchdata'),
    path('update/<int:id>', views.update, name='update')
]
