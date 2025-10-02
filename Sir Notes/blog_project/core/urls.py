from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', view=views.get_blogs, name="get_blogs"),
    path('blogs/<int:blog_id>', view=views.get_blog, name='get_blog'),
    path('blogs/<int:blog_id>/create', view=views.create_comment, name='create_comment'),
]