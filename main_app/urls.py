from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("about/", views.about, name="about"),
    path("api/",views.api, name="api"),
    path("bins/", views.bins_index, name="bins_index"),
    path("bins/<int:bin_id>/", views.bins_detail, name="detail"),
    # path("bins/<int:bin_id>/delete", views.bins_delete, name="bins_delete"),
    # path("bins/<int:bin_id>/edit", views.bins_edit, name="bins_edit"),
]