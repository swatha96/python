from django.urls import path
from . import views
urlpatterns = [
    path("",views.show),
    path("show/",views.show),
    path("add/",views.emp),
    path("edit/<int:empid>",views.edit),
    path("delete/<int:empid>",views.remove),
    path("update/<int:empid>",views.update),
]
