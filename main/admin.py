from django.contrib import admin
from .models import Event, Article, Gallery, GalleryItem, EventType, Ticket, TicketType, EventTestimonial, EventTestimonialAttachment

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = ['event_name', 'event_description',]
    prepopulated_fields = {'slug' : ['event_name', ]}
    list_display = ['event_name', 'event_venue', 'event_date', 'event_type']
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['article_title', 'article_tags', 'article_author']
    prepopulated_fields = {'slug': ['article_title', ]}
    readonly_fields = ['article_publish', 'article_modified',]
    list_display = ['article_title', 'article_publish', 'article_author']

@admin.register(Gallery)
class Gallery(admin.ModelAdmin):
    list_filter = ['gallery_name', 'gallery_description', 'gallery_author', ]
    prepopulated_fields = {'slug': ['gallery_name', ]}
    list_display = ['gallery_name', 'gallery_author']
    
@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_filter = ['gallery_item_name', 'gallery_item_image', ]
    prepopulated_fields = {'slug': ['gallery_item_name', ]}
    list_display = ['gallery_item_name', 'gallery', ]
    
@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['event_type_name', ]

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_filter = ['ticket_name', 'ticket_description', ]
    list_display = ['ticket_name', 'ticket_price', 'ticket_type', 'event']
    
@admin.register(TicketType)
class TicketTypeAdmin(admin.ModelAdmin):
    list_filter = ['ticket_type_name', ]
    list_display = ['ticket_type_name']
    
@admin.register(EventTestimonial)
class EventTestimonialAdmin(admin.ModelAdmin):
    list_display = ['event', 'testimonial_author', 'event_rate', 'testimonial_publish',]
    list_filter = ['event_rate', 'testimonial_publish', 'testimonial_author', ]
    filter_horizontal = ['testimonial_attachments', ]

@admin.register(EventTestimonialAttachment)
class EventTestimonialAttachmentAdmin(admin.ModelAdmin):
    list_display = ['testimonial_attachment', ]