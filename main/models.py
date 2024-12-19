from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from .tags import MetaTagsAll
from django.utils.text import slugify
# Create your models here.

class Event(models.Model):
    meta_description = models.CharField(max_length=500, verbose_name='Метаданные страницы - ОПИСАНИЕ', help_text='Описание нужно чтобы поисковики по типу гугла или яндекса могли искать и показывать наш сайт если ввели какой то запрос по типу названия события')
    meta_keywords = TaggableManager(verbose_name='Метаданные страницы - КЛЮЧЕВЫЕ СЛОВА', help_text='Ключевые слова нужны чтобы поисковики по типу гугла или яндекса могли искать и показывать наш сайт ишя по ключевым словам. ЧЕРЕЗ ЗАПЯТУЮ (НАПРИМЕР: Концерт, Садраддин, Новый год, ...).')
    
    event_name = models.CharField(max_length=100, verbose_name='Название ивента')
    event_description = RichTextField(verbose_name='Описание ивента', help_text='Описание ивента. Он будет отображаться на сайте')
    event_poster = models.ImageField(verbose_name='Постер ивента', help_text='Размеры постера 500px × 700px', upload_to='event/posters/')
    event_venue = models.CharField(max_length=100, verbose_name='Место проведения')
    event_date = models.DateField(verbose_name='Дата проведения')
    event_start_time = models.TimeField(verbose_name='Начало', help_text='Во сколько начнеться ивент')
    event_duration = models.DurationField(verbose_name='Продолжительность', help_text='Продолжительность ивента')
    AGE_LIMIT_CHOICES = {
        '6+' : '6+',
        '12+' : '12+',
        '16+' : '16+',
        '18+' : '18+',
        '21+' : '21+'
    }
    event_age_limit = models.CharField(max_length=3,choices=AGE_LIMIT_CHOICES, verbose_name='Возрастное ограничение')
    event_type = models.ForeignKey(to='main.EventType', on_delete=models.CASCADE, verbose_name='Тип ивента')
    
    slug = models.SlugField(verbose_name='Ссылка', help_text='Автоматический генерируется')

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.event_name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.event_name}'
    
    
    class Meta:
        verbose_name = 'Ивент'
        verbose_name_plural = 'Ивенты'

class Article(models.Model):
    meta_description = models.CharField(max_length=500, verbose_name='Метаданные страницы - ОПИСАНИЕ', help_text='Описание нужно чтобы поисковики по типу гугла или яндекса могли искать и показывать наш сайт если ввели какой то запрос по типу названия события')
    meta_keywords = TaggableManager(verbose_name='Метаданные страницы - КЛЮЧЕВЫЕ СЛОВА', help_text='Ключевые слова нужны чтобы поисковики по типу гугла или яндекса могли искать и показывать наш сайт ишя по ключевым словам. ЧЕРЕЗ ЗАПЯТУЮ (НАПРИМЕР: Концерт, Садраддин, Новый год, ...).')
    
    
    article_title = models.CharField(max_length=150, verbose_name='Названия статьи')
    article_content = RichTextField(verbose_name='Контент статьи')
    article_tags = TaggableManager(verbose_name='Теги статьи', help_text='Теги для статьи нужны чтобы сортировать, группировать, а так же для удобного поиска и фильтрации', through=MetaTagsAll)
    article_publish = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    article_modified = models.DateTimeField(auto_now=True, verbose_name='Время редактирования', help_text='Время последнего редактирования статьи', blank=True)
    article_author = models.CharField(max_length=150)
    
    slug = models.SlugField(verbose_name='Ссылка', help_text='Автоматический генерируется')
    
    
    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.article_title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.article_title} by {self.article_author} [{self.article_publish}]'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        
        
class Gallery(models.Model):
    meta_description = models.CharField(max_length=500, verbose_name='Метаданные страницы - ОПИСАНИЕ', help_text='Описание нужно чтобы поисковики по типу гугла или яндекса могли искать и показывать наш сайт если ввели какой то запрос по типу названия события')
    meta_keywords = TaggableManager(verbose_name='Метаданные страницы - КЛЮЧЕВЫЕ СЛОВА', help_text='Ключевые слова нужны чтобы поисковики по типу гугла или яндекса могли искать и показывать наш сайт ишя по ключевым словам. ЧЕРЕЗ ЗАПЯТУЮ (НАПРИМЕР: Концерт, Садраддин, Новый год, ...).')
    
    
    gallery_name = models.CharField(max_length=150, verbose_name='Названия галереи')
    gallery_description = RichTextField(verbose_name='Описание галереи')
    gallery_author = models.CharField(max_length=150, verbose_name='Автор галереи')

    slug = models.SlugField(verbose_name='Ссылка', help_text='Автоматический генерируется')
    
    
    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.gallery_name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.gallery_name}'
    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

class GalleryItem(models.Model):
    gallery_item_name = models.CharField(max_length=100, verbose_name='Название медиа', help_text='')
    gallery_item_image = models.ImageField(upload_to='gallery/images/', verbose_name='Фотография', help_text='Любая медия но не все')
    gallery = models.ForeignKey(to='main.Gallery', verbose_name='Галерея', help_text='Принодлежность к какому то галерее', on_delete=models.CASCADE)
    
    slug = models.SlugField(verbose_name='Ссылка', help_text='Автоматический генерируется')
    
    
    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.gallery_item_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.gallery_item_name} из колекции галереи {self.gallery} от {self.gallery.gallery_author}'
    
    class Meta:
        verbose_name = 'Обьект галереи'
        verbose_name_plural = 'Обьекты галереи'
        

class EventType(models.Model):
    event_type_name = models.CharField(max_length=100, verbose_name='Названия типа ивента')
    
    def __str__(self):
        return f'{self.event_type_name}'
    
    class Meta:
        verbose_name = 'Тип ивента'
        verbose_name_plural = 'Типы ивентов'
    


class Ticket(models.Model):
    ticket_name = models.CharField(max_length=150, verbose_name='Название билета')
    ticket_description = RichTextField(verbose_name='Описание билета', help_text='Опишите что входит в услуги')
    
    ticket_price = models.IntegerField(verbose_name='Цена билета', help_text='Местная валюта (Тенге - KZT)')
    ticket_type = models.ForeignKey(to='main.TicketType', on_delete=models.CASCADE, verbose_name='Тип билета')
    
    event = models.ForeignKey(to='main.Event', verbose_name='Билет Ивента', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.ticket_name} - {self.ticket_price}'
    
    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        
class TicketType(models.Model):
    ticket_type_name = models.CharField(max_length=150, verbose_name='Названия типа билета', help_text='Например VIP, Закулисье, Фанзона и тд')
    
    def __str__(self):
        return f'{self.ticket_type_name}'
    
    class Meta:
        verbose_name = 'Тип билета'
        verbose_name_plural = 'Типы билетов'
        
class EventTestimonial(models.Model):
    event = models.ForeignKey(to='main.Event', verbose_name='Ивент', on_delete=models.CASCADE)
    testimonial_author = models.CharField(max_length=150, verbose_name='Автор')
    testimonial_content = models.CharField(max_length=200, verbose_name='Отзыв')
    EVENT_RATE_CHOICES = {
        0 : 0,
        1 : 1,
        2 : 2,
        3 : 3,
        4 : 4,
        5 : 5
    }
    event_rate = models.IntegerField(default=0, choices=EVENT_RATE_CHOICES, verbose_name='Оценка ивента')
    testimonial_publish = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    testimonial_attachments = models.ManyToManyField(to='main.EventTestimonialAttachment', blank=True, verbose_name='Прикрепленные фотографии')

    def __str__(self):
        return f'Отзыв от {self.testimonial_author} в {self.testimonial_publish}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class EventTestimonialAttachment(models.Model):
    testimonial_attachment = models.ImageField(verbose_name='Прикепленная фотография', upload_to='testimonial/attachment/')
    
    class Meta:
        verbose_name = 'Прикрепленный к отзыву фото'
        verbose_name_plural = 'Прикрепленные к отзывам фотографии'
    
    