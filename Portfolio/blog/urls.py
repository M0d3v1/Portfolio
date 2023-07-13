from django.urls import path
from .views import (
    show_blogs,
    details
)



urlpatterns = [
    path('', show_blogs, name="show_blogs"),
    path('<int:blog_id>/', details, name="details")
]