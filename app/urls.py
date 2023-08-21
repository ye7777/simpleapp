from django.urls import path
from .views import HelloView

app_name = "app"
urlpatterns = [
    path("",HelloView.as_view(),name="hello")
]