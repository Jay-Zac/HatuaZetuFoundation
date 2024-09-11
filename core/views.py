from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from .models import Blog, UserMessage, Project
from .forms import UserMessageForm


# Home page view: Displays the homepage with recent projects
def home_page_view(request):
    try:
        # Fetch the latest 4 projects from the database
        recent_projects = Project.objects.all()[:4]
        context = {'recent_projects': recent_projects}
    except Project.DoesNotExist:
        # Handle case where no projects are found
        messages.error(request, "No recent projects available.")
        context = {'recent_projects': []}
    except Exception as e:
        # Handle any other unexpected errors
        messages.error(request, f"An unexpected error occurred: {e}")
        context = {'recent_projects': []}

    return render(request, 'core_html/homepage.html', context)


# Engagements page view: Renders the engagements page
def engagements_view(request):
    try:
        return render(request, 'core_html/engagements.html')
    except Exception as e:
        # Handle errors during page rendering
        messages.error(request, f"Error loading engagements page: {e}")
        return render(request, 'core_html/engagements.html')


# About Us page view: Renders the About Us page
def about_us_view(request):
    try:
        return render(request, 'core_html/about_us.html')
    except Exception as e:
        # Handle errors during page rendering
        messages.error(request, f"Error accessing About Us page: {e}")
        return render(request, 'core_html/about_us.html')


# Contact Us page view: Handles form submission for user messages
def contact_us_view(request):
    form = UserMessageForm()  # Instantiate a new form object

    if request.method == 'POST':
        form = UserMessageForm(request.POST)  # Bind the POST data to the form

        if form.is_valid():
            try:
                # Save the form data as a new UserMessage entry
                cleaned = form.cleaned_data
                user_message = UserMessage(
                    first_name=cleaned['first_name'],
                    last_name=cleaned['last_name'],
                    email=cleaned['email'],
                    message=cleaned['message'],
                )
                user_message.save()

                # Success message
                messages.success(request, "Your message has been sent successfully!")
                return JsonResponse({'message': 'success'})

            except Exception as e:
                # Handle errors while saving the message
                messages.error(request, f"An error occurred while saving your message: {e}")
        # Form validation errors
        messages.error(request, "Invalid form data. Please correct the errors below.")

    # Render the Contact Us page with the form
    return render(request, 'core_html/contact_us.html', {'form': form})


# More Projects page view: Displays projects beyond the initial 4
def more_projects_view(request):
    more_projects = Project.objects.all()[4:]  # Fetch projects starting from the 5th entry
    return render(request, 'core_html/more_projects.html', {'more_projects': more_projects})


# Project detail view: Shows details of a specific project
def project_detail_view(request, pk):
    try:
        # Retrieve the project entry by primary key
        project = Project.objects.get(id=pk)
        context = {'project': project}
    except Project.DoesNotExist:
        # Handle case where the project does not exist
        messages.error(request, "Project not found.")
        context = {'project': None}
    except Exception as e:
        # Handle any other unexpected errors
        messages.error(request, f"Error retrieving project: {e}")
        context = {'project': None}

    return render(request, 'core_html/project_detail.html', context)


# All Blogs page view: Displays all blog entries
def all_blogs_view(request):
    try:
        # Retrieve all blog entries
        blogs = Blog.objects.all()
        context = {'blogs': blogs}
    except Blog.DoesNotExist:
        # Handle case where no blogs are found
        messages.error(request, "No blogs available.")
        context = {'blogs': []}
    except Exception as e:
        # Handle any other unexpected errors
        messages.error(request, f"An unexpected error occurred: {e}")
        context = {'blogs': []}

    return render(request, 'core_html/blog_page.html', context)


# Blog detail view: Shows details of a specific blog post
def blog_detail_view(request, pk):
    try:
        # Retrieve the blog entry by primary key
        blog = Blog.objects.get(id=pk)
        context = {'blog': blog}
    except Blog.DoesNotExist:
        # Handle case where the blog does not exist
        messages.error(request, "Blog not found.")
        context = {'blog': None}
    except Exception as e:
        # Handle any other unexpected errors
        messages.error(request, f"Error retrieving blog: {e}")
        context = {'blog': None}

    return render(request, 'core_html/blog_detail.html', context)
