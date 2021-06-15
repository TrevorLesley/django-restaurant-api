from django.urls import path, include

urlpatterns = [
    path("dishes/", include("dishes.urls")),
]
