from . import views
from django.urls import path


urlpatterns = [
    path('', views.products_view, name='products_view'),
    path('<slug:slug>-<int:pk>', views.products_details, name='product_details'),
    path('<int:pk>', views.products_filter, name='by_category'),

]