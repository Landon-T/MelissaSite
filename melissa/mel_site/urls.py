from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    #path("register", views.register, name="register"),
    path("meet", views.meet, name="meet"),
    path("speak", views.speak, name="speak"),
    path("involved", views.involved, name="involved"),
    path("store", views.store, name="store"),
    path("create",views.create, name="create"),
    path("edit/<str:title>",views.edit, name="edit")

]