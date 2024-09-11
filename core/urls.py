from django.urls import path
from . import views

# App name for namespacing URL names
app_name = 'core'

urlpatterns = [
    path('', views.home_page_view, name='home'),  # Home page
    path('engagements/', views.engagements_view, name='strategic_engagements'),  # Engagements page
    path('all-blogs/', views.all_blogs_view, name='all_blogs'),  # All blogs page
    path('blog/<int:pk>/', views.blog_detail_view, name='blog_detail'),  # Blog detail
    path('about-us/', views.about_us_view, name='about'),  # About page
    path('contact-us/', views.contact_us_view, name='contact'),  # Contact page
    path('more-projects/', views.more_projects_view, name='more_projects'),  # More projects page
    path('project/<int:pk>/', views.project_detail_view, name='project_detail'),  # Project detail
]
