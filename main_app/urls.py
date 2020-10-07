from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("about/", views.about, name="about"),
    path("api/",views.api, name="api"),
    path("bins/", views.bins_index, name="bins_index"),
    path("bins/<int:bin_id>/", views.bins_detail, name="bin_detail"),
    path("bins/<int:bin_id>/delete", views.bins_delete, name="bins_delete"),
    path("bins/<int:bin_id>/edit", views.bins_edit, name="bins_edit"),
    path("businesses/", views.businesses_index, name="businesses_index"),
    path("businesses/<int:business_id>/", views.businesses_detail, name="business_detail"),
    path("persons/", views.persons_index, name="person_index"),
    path("persons/<int:person_id>/", views.persons_detail, name="person_detail"),
    path("collection_markets/", views.collection_markets_index, name="collection_markets_index"),
    path("collection_markets/<int:collection_market_id>/", views.collection_markets_detail, name="collection_market_detail"),
]