from django.urls import re_path
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'shop'

urlpatterns = [
    re_path('categories/(?P<pk>[\w_-]+)/', cache_page(60)(views.CategoryView.as_view()), name='category'),
    re_path('products/',csrf_exempt(views.ProductView.as_view()), name='products')

]
