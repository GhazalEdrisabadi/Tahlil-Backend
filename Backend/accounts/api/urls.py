from django.conf.urls import url
from django.conf.urls.static import static
from accounts.api.views import UserLoginAPIView, UserCreateAPIView
from Backend import settings

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
