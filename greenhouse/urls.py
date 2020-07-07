from django.urls import path

from . import views

app_name = 'greenhouse'
urlpatterns = [
    path('', views.index, name='index'),
    path('json/<str:v_id>', views.JsonView.as_view()),
]
