from django.conf.urls import path, include
from django.contrib import admin
from vocabsearch import views

urlpatterns = [
    path('/', views.IndexView.as_view(), name="index"),
    path('test/', views.init_test, name="init_test"),
    path('test/<type:string>/<amount:int>/<direction:string>/', views.TakeTest.as_view(), name="take_test"),
    path('admin/', admin.site.urls),
]
