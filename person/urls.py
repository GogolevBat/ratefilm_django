from django.urls import path
from . import views
urlpatterns = [
    path('<int:person_id>/', views.person_show),

    path('<int:person_id>/favoriteit', views.person_favorite_it),

    path('<int:person_id>/favoriteout', views.person_favorite_out),

    path('<int:person_id>/mini', views.person_show_mini),

]