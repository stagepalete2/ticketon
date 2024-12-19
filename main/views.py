from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
# Create your views here.



class HomePage(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            
        )
        
        return context

class EventsPage(TemplateView):
    template_name = 'pages/events.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            
        )
        
        return context
    
class EventDetailPage(DetailView):
    template_name = 'pages/detail/single_event.html'
    context_object_name = 'event'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            
        )
        
        return context
        
        
class BlogPage(TemplateView):
    template_name = 'pages/blog.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            
        )
        
        return context
    
class BlogAuthorDetailPage(DetailView):
    template_name = 'pages/detail/blog_author.html'
    context_object_name = 'author'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            
        )
        
        return context
    
class ArticlePage(DetailView):
    template_name = 'pages/detail/blog_article.html'
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
            
        )
        
        return context
    
class GalleryDetailPage(DetailView):
    template_name = 'pages/detail/detail_gallery.html'
    context_object_name = 'gallery'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            
        )
        
        return context