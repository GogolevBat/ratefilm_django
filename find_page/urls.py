from django.urls import path
from . import views
urlpatterns = [
    path('', views.find_main, name='find_page'),
    path('java_find/title', views.java_find_title),
    path('java_find/person', views.java_find_person),

    path('java_find/mini', views.find_mini),

]
