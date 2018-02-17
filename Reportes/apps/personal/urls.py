from django.conf.urls import url
from apps.personal import views

urlpatterns = [
    url(r'^personal/$', views.personal_list),
]
