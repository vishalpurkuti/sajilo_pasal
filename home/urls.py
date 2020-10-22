from django.urls import path
from . import views

urlpatterns=[
    path('',views.ListView.as_view(),name='home'),
    path('<int:id>',views.DetailView.as_view(),name="product_detail")
]