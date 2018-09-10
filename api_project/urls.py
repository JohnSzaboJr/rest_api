from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^Cities/$', CreateView.as_view(), name="create"),
    url(r'^Cities/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
