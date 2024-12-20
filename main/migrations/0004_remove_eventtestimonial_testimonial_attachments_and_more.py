# Generated by Django 5.1.4 on 2024-12-20 03:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_event_event_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventtestimonial',
            name='testimonial_attachments',
        ),
        migrations.AddField(
            model_name='eventtestimonialattachment',
            name='testimonial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.eventtestimonial', verbose_name='Отзыв'),
            preserve_default=False,
        ),
    ]