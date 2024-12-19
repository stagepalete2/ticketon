from django.urls import path
from .views import HomePage, EventsPage, EventDetailPage, BlogPage, BlogAuthorDetailPage, ArticlePage, GalleryPage, GalleryDetailPage


urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    
    path('events/', EventsPage.as_view(), name='events_page'),
    path('event/<slug:slug>/', EventDetailPage.as_view(), name='event_detail_page'),
    
    path('blog/', BlogPage.as_view(), name='blog_page'),
    path('blog/<slug:slug>/', BlogAuthorDetailPage.as_view(), name='blog_author_detail_page'),
    path('blog/<slug:author>/<slug:article>/', ArticlePage.as_view(), name='blog_article_detail_page'),
    
    
    path('gallery/', GalleryPage.as_view(), name='gallery_page'),
    path('gallery/<slug:slug>/', GalleryDetailPage.as_view(), name='gallery_detail_page'),
    
]
