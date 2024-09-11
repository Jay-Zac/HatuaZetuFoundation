from django.db import models


# Blog model
class Blog(models.Model):
    DoesNotExist = None  # For unresolved attribute referencing
    objects = None  # For unresolved attribute referencing
    image = models.ImageField(upload_to='blogs_images')  # Image field
    title = models.CharField(max_length=200)  # Title field
    content = models.TextField()  # Content field
    external_reference = models.CharField(max_length=2083, blank=True)  # Optional external reference
    date_and_time_created = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    class Meta:
        ordering = ('-date_and_time_created',)  # Default ordering


# UserMessage model
class UserMessage(models.Model):
    first_name = models.CharField(max_length=50)  # First name
    last_name = models.CharField(max_length=50)  # Last name
    email = models.EmailField()  # Email address
    message = models.TextField()  # User message
    date_and_time_created = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    class Meta:
        ordering = ('-date_and_time_created',)  # Default ordering


# Project model
class Project(models.Model):
    DoesNotExist = None  # For unresolved attribute referencing
    objects = None  # For unresolved attribute referencing
    image = models.ImageField(upload_to='projects_images')  # Image field
    title = models.CharField(max_length=200)  # Title field
    content = models.TextField()  # Content field
    external_reference = models.CharField(max_length=2083, blank=True)  # Optional external reference
    date_and_time_created = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    class Meta:
        ordering = ('-date_and_time_created',)  # Default ordering
