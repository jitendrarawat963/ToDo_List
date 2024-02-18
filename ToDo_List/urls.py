from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('complete/<int:id>/',views.updatePage,name='complete'),
    path('delete/<int:id>/',views.deletePage),
]
