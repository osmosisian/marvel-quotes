from django.urls import path

from . import views

urlpatterns = [
    path("",views.index),
    path("<int:month>", views.monthly_challange_by_number),
    path("<str:character>", views.monthly_challange,name="quotes")
]
