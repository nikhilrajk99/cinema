from . import views
from django.urls import path
app_name='cinemaapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add',views.add_movie,name='add_movie')
]