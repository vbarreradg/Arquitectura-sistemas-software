from django.urls import path

from . import views


urlpatterns = [
    #path('', views.index, name='index'), #para la vista index
    path('', views.comments_all, name='all'),
    path('<int:com_id>/', views.detail, name='detail'),
    path('comentar/', views.comentar, name='comment'),
]