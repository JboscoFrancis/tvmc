from django.db import models
from django.forms import ValidationError
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class News(models.Model):
    PRIORITY_CHOICES = [
        ('higher', 'Higher'),
        ('medium', 'Medium')
    ]
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 0.3
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Opps!, Maximum allowed image size is %sMB" % str(megabyte_limit))
        
    title = models.CharField(max_length=156)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium', help_text='if News set to higher priority, will always be displayed in page')
    body = CKEditor5Field(max_length=12500)
    thumbnail = models.ImageField(upload_to='news_thumbnail', validators=[validate_image])
    slug = models.SlugField(max_length=256, unique=True, blank=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_news', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='updated_news', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='News'
        ordering = ['-date_created']
        
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while News.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter+=1
            self.slug = slug
        else:
            update_slug = slugify(self.title)
            slug = update_slug
            counter = 1
            while News.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{update_slug}-{counter}"
                counter+=1
            self.slug = slug

        super().save(*args, **kwargs)

