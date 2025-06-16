from django.contrib import admin
from django.urls import path, include
from my_admin_logs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_menu.urls')),
    path('find/', include('find_page.urls')),

    path('title/', include('title.urls')),
    path('person/', include('person.urls')),

    path('accounts/', include('users.urls')),

]


