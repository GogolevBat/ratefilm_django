from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.sign_up, name='registration'),
    path('register/', views.register_menu, name='register'),

    path('profile/<str:profile_hash_user_id>', views.profile),

    path('profile/<str:profile_hash_user_id>/favorites', views.user_favorites),

    path('profile/<str:profile_hash_user_id>/reviews', views.user_reviews),

    path('profile/<str:profile_hash_user_id>/review/<int:movie_id>', views.user_review_show),
    path('profile/<str:profile_hash_user_id>/review/<int:movie_id>/reaction', views.user_reaction),
    path('change/nickname', views.change_nickname),
    path('change/block', views.change_block),

    path('profile/<str:profile_hash_user_id>/review/<int:movie_id>/change/', views.change_review),


]