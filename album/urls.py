from django.conf.urls import url
from album import views

urlpatterns = [
    url(r'^$', views.first_view, name="first-view"),
    url(r'^category/$', views.category, name="category-list"),
    url(r'^category/(?P<category_id>[0-9]+)/detail/$', views.category_detail, name="category-detail"),
    url(r'^photo/$', views.PhotoListView.as_view(),name="photo-list"),
    url(r'^photo/$, (?P<pk>[0-9]+)/detail/$',views.PhotoDetailView.as_view(), name="photo-detail"),
]
