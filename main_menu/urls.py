from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),

    path('add/content', views.add_content_on_menu),

    path('about-us', views.about, name='about'),
    path('pin', views.pined, name='user_pined'),

    path('viewed', views.viewed, name='viewed'),
    path('favorites', views.favorited, name='favorites'),


]
