from django.contrib import admin
from django.urls import path
from bulb import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('powerofbulb/',views.power_calculate,name="powerofbulb"),
    path('',views.power_calculate,name="powerofbulb")
]