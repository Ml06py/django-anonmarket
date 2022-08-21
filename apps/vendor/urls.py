from django.urls import  path
from . import views

app_name = "vendor"

urlpatterns = [
    path("add-product/", views.AddProduct.as_view(), name="add-product"),
    path("update-product/<int:id>/<str:slug>/", views.UpdateProduct.as_view(), name="update-product"),

]