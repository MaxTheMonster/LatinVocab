import vocabulary.views as vocabulary
import literature
#import literature.views as literature

from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', vocabulary.IndexView.as_view(), name="index"),
    path('test/', vocabulary.init_test, name="test"),
#    path('test/<str:type>/<int:amount>/<str:direction>/', vocabulary.TakeTest.as_view(), name="take_test"),
    path('literature/', include('literature.urls')),
    path('admin/', admin.site.urls),
]
