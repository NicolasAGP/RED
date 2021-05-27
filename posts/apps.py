"""Posts application module."""

from django.apps import AppConfig


class PostsConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    """Posts application settings"""
    name = 'posts'
    varbose_name = 'Posts'
