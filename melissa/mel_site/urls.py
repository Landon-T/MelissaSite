from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("meet", views.meet, name="meet"),
    path("speak", views.speak, name="speak"),
    path("involved", views.involved, name="involved"),
    path("store", views.store, name="store"),
    path("create",views.create, name="create")
]