from django.urls import path
from .views import HomePage, EventsPage, EventDetailPage, BlogPage, ArticlePage, GalleryPage, GalleryDetailPage, GetTestimonial, ProfilePage, SignUpView, FAQPage, AboutPage, ArtistsPage, ArtistDetailPage, ArtistSongDetailPage, SearchPage
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    
    path('events/', EventsPage.as_view(), name='events_page'),
    path('event/<slug:slug>/', EventDetailPage.as_view(), name='event_detail_page'),
    
    path('blog/', BlogPage.as_view(), name='blog_page'),
    path('blog/<slug:slug>/', ArticlePage.as_view(), name='blog_article_detail_page'),
    
    
    path('gallery/', GalleryPage.as_view(), name='gallery_page'),
    path('gallery/<slug:slug>/', GalleryDetailPage.as_view(), name='gallery_detail_page'),
    
    path('artists/', ArtistsPage.as_view(), name='artists_page'),
    path('artist/<slug:slug>/', ArtistDetailPage.as_view(), name='artists_detail_page'),
    path('artistsong/<slug:slug>/', ArtistSongDetailPage.as_view(), name='artists_song_detail_page'),
    
    path('search/', SearchPage.as_view(), name='search'),
    
    path('profile/<int:pk>/', ProfilePage.as_view(), name='profile'),
    path('profile/login/', auth_views.LoginView.as_view(template_name='pages/signin.html'), name='signin'),
    path('profile/signup/', SignUpView.as_view(), name='signup'),
    path('profile/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('faqs/', FAQPage.as_view(), name='faq'),
    path('aboutus/', AboutPage.as_view(), name='aboutus'),

    
    path('api/get-testimonial/', GetTestimonial.as_view(), name='api_get_testimonial'),
    

]
