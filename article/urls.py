from django.urls import path
from article import views
app_name = "art"
urlpatterns = [
    path('', views.articles, name = "articles"),
    path('about/', views.about, name = "about"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.addarticle, name="addarticle"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('update/<int:id>/', views.articleUpdate, name="update"),
    path('delete/<int:id>/', views.articleDelete, name="delete"),
    path('comment/<int:id>/', views.commentAdd, name="addcomment"),
]
