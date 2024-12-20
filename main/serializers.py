from rest_framework import serializers
from django import forms
from .models import EventTestimonial, EventTestimonialAttachment

# Serializer for Attachments
class EventTestimonialAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTestimonialAttachment
        fields = '__all__'

# Serializer for Testimonials
class TestimonialSerializer(serializers.ModelSerializer):
    images = EventTestimonialAttachmentSerializer(many=True, read_only=True)
    testimonial_attachments = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = EventTestimonial
        fields = ['event', 'testimonial_author', 'testimonial_content', 'event_rate', 'images', 'testimonial_attachments']

    def create(self, validated_data):
        uploaded_images = validated_data.pop("testimonial_attachments")
        testimonial = EventTestimonial.objects.create(**validated_data)

        for image in uploaded_images:
            EventTestimonialAttachment.objects.create(testimonial=testimonial, testimonial_attachment=image)

        return testimonial