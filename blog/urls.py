from django.urls import path  # path для создания путей
from . import views  # импорт представлений


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
