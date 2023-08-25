from django.urls import path
from .views import HelloView,NameformView,ListView

app_name = "app"
urlpatterns = [
    path("",HelloView.as_view(),name="hello"),
    path("form/",NameformView.as_view(),name="form"),
    path("list/",ListView.as_view(),name="list"),
]
