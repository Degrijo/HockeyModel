from django.urls import path, include

urlpatterns = [
    path('core/', include('core.urls')),
]
