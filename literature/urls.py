from django.urls import path
from literature import views

urlpatterns = [
    path('', views.LiteratureView.as_view(), name="literature")
]
