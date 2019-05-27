"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from article import urls as article_urls
from user import urls as user_urls

#For Media files
from django.conf import settings
from django.conf.urls.static import static
from article.views import index,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/',include(article_urls)),
    path('user/',include(user_urls)),
    path('',index, name = "index"),
    path('about/',about, name = "about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)