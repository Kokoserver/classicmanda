
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('home.urls')),
    path('account/', include('customer.urls')),
    path('admin/', admin.site.urls),
]
