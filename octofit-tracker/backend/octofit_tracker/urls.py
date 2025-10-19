"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.http import JsonResponse
from django.urls import path
from django.contrib import admin

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    return JsonResponse({
        "activities": f"{base_url}activities/",
        "teams": f"{base_url}teams/",
        "users": f"{base_url}users/",
        "leaderboard": f"{base_url}leaderboard/",
        "workouts": f"{base_url}workouts/"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
]
