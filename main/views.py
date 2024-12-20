from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, DetailView, CreateView
from django.db.models.functions import Trunc
from django.utils.timezone import now
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
# Create your views here.
from .models import AboutUs, Album, Artist, Event, Article, FAQs, Gallery, GalleryItem, HomePageModel, Song, Ticket, EventTestimonial, EventTestimonialAttachment, UserOrder, GalleryItemComment
from .serializers import TestimonialSerializer, EventTestimonialAttachmentSerializer
from .forms import RegistrationForm

from django.contrib.auth.models import User
from django.contrib.auth import login

class HomePage(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        banners = []
        banner1 = []
        banner2 = []
        
        # Check if HomePageModel has any objects
        homepage = HomePageModel.objects.first()  # Get the first object
        if homepage:
            banners = homepage.banner.all()  # Retrieve related banners
            if banners.exists():
                # Split banners into two halves
                banner1 = banners[:len(banners)//2]
                banner2 = banners[len(banners)//2:]

        # Add data to context
        context.update(
            events=Event.objects.all(),
            articles=Article.objects.all(),
            banner1=banner1,
            banner2=banner2
        )
        
        return context


class EventsPage(TemplateView):
    template_name = 'pages/events.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        events = Event.objects.all()
        days = [event.event_date for event in events.distinct('event_date')]
        tickets = Ticket.objects.all()
        events = events.annotate(key=Trunc('event_date', 'days')).order_by('key').filter(event_date__gte=now())
        
        for event in events:
            start_price = tickets.filter(event=event).order_by('ticket_price').first()
            event.start_price = start_price.ticket_price if start_price else 0
        
        
        context.update(
            events = events,
            days = days,
        )
        
        return context
    
class EventDetailPage(DetailView):
    template_name = 'pages/detail/single_event.html'
    model = Event
    context_object_name = 'event'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = EventTestimonial.objects.filter(event=self.object).order_by('-testimonial_publish')
        
        if self.request.user and self.request.user.is_authenticated:
            user_order = UserOrder.objects.filter(user=self.request.user ,ticket__event=self.object)
        
        for testimonial in testimonials:
            testimonial.testimonial_attachments = [photo.testimonial_attachment for photo in EventTestimonialAttachment.objects.filter(testimonial=testimonial)]
            
        context.update(
            testimonials = testimonials,
            user_order = user_order 
        )
        
        return context
        
class ProfilePage(DetailView):
    template_name = 'pages/detail/profile.html'
    model = User
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update(
            tickets = UserOrder.objects.filter(user=self.request.user)
        )
        
        return context


class BlogPage(TemplateView):
    template_name = 'pages/blog.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update(
            articles = Article.objects.all(),
        )
        
        return context
    
class SignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'pages/signup.html'
    success_url = reverse_lazy('signin')

    def get_success_url(self) -> str:
        success_url = super().get_success_url()
        success_url += f'?isFormValid={True}'
        return success_url

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        self.isFormValid = False
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            SignUpForm = self.form_class
        )
        return context
    

class ArticlePage(DetailView):
    template_name = 'pages/detail/blog_article.html'
    model = Article
    context_object_name = 'article'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            
        )
        
        return context
    
    
class GalleryPage(TemplateView):
    template_name = 'pages/gallery.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            galleries = Gallery.objects.all(),
        )
        
        return context
    
class GalleryDetailPage(DetailView):
    template_name = 'pages/detail/detail_gallery.html'
    model = Gallery
    context_object_name = 'gallery'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        items = GalleryItem.objects.all().filter(gallery=self.object)
        
        for item in items:
            item.comments = GalleryItemComment.objects.filter(gallery_item=item).order_by('-testimonial_publish')
        
        
        context.update(
            items = items,
        )
        
        
        return context
    
    
class GetTestimonial(CreateAPIView):
    def post(self, request, format=None):
        serializer = TestimonialSerializer(data=request.data)
        if serializer.is_valid():
            testimonial = serializer.save()
            referer = request.META.get('HTTP_REFERER', '/')  # Fallback to root if HTTP_REFERER is not present
            return redirect(referer)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class FAQPage(TemplateView):
    template_name = 'pages/faq.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update(
            faqs = FAQs.objects.all(),
        )
        
        return context
    
class AboutPage(TemplateView):
    template_name = 'pages/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update(
            about = AboutUs.objects.first(),
        )
        
        return context
    

class ArtistsPage(TemplateView):
    template_name = 'pages/artists.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        artists = Artist.objects.all()
        if self.request.GET.get('artist_name'):
            artists = artists.filter(nickname=self.request.GET.get('artist_name'))
        
        context.update(
            artists = artists
        )
        
        return context
    
class ArtistDetailPage(DetailView):
    template_name = 'pages/detail/artist_detail.html' 
    model = Artist
    context_object_name = 'artist'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update(
            songs = Song.objects.filter(artist=self.object.id).distinct(),
            albums = Album.objects.filter(artist=self.object.id).distinct(),
            events = Event.objects.filter(artists=self.object.id).distinct(),
        )
        
        return context
    
class ArtistSongDetailPage(DetailView):
    template_name = 'pages/detail/artist_song_detail.html'
    model = Song
    context_object_name = 'song'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update(
        )
        
        return context
    
class SearchPage(TemplateView):
    template_name = 'pages/search.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the search query from the request
        q = self.request.GET.get('q')
        
        # Initialize search results
        events = []
        artists = []
        songs = []
        articles = []
        
        if q:
            print(q)
            # Search events (allow partial match)
            events = Event.objects.filter(
                Q(event_name__icontains=q) |
                Q(artists__nickname__icontains=q)
            ).order_by('-event_date').distinct()
            
            # Search artists (allow partial match on name or nickname)
            artists = Artist.objects.filter(
                Q(name__icontains=q) |
                Q(nickname__icontains=q)
            ).distinct()
            
            # Search songs (allow partial match on name)
            songs = Song.objects.filter(
                Q(name__icontains=q)
            ).distinct()
            
            # Search articles (allow partial match on title or author)
            articles = Article.objects.filter(
                Q(article_title__icontains=q) |
                Q(article_author__icontains=q)
            ).distinct()
        
        # Update the context with search results
        context.update({
            'events': events,
            'artists': artists,
            'songs': songs,
            'articles': articles,
            'query': q,  # Pass the search query to the template
        })
        
        return context