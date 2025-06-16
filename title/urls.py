from django.urls import path
from . import views
urlpatterns = [
    path('<int:title_id>/', views.title_show),
    path('<int:title_id>/rate/', views.save_rating),
    path('<int:title_id>/review/', views.save_review),

    path('<int:title_id>/pinit/', views.save_pin),
    path('<int:title_id>/pinout/', views.delete_pin),

    path('<int:title_id>/favoriteit/', views.save_favorite),
    path('<int:title_id>/favoriteout/', views.delete_favorite),

    path('<int:title_id>/reviews', views.show_reviews),


]
