from django.urls import path
from .views import *

urlpatterns = [
    path("article/<uuid:article_id>/", ResponseListCreateView.as_view(), name="article_responses"),
    path("<uuid:id>/", ResponseUpdateDeleteView.as_view(), name="response_detail")
]
