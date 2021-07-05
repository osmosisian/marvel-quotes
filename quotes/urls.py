from django.urls import path

from . import views

urlpatterns = [
    path("",views.index),
    path("<int:month>", views.quotes_by_number),
    path("<str:character>", views.quotes_display,name="quotes")
]
