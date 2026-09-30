from django.contrib import admin
from django.urls import path, include

#Url del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diario_user.urls'))
]
