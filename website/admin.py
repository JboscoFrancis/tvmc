from django.contrib import admin
from website.models import News

# Register your models here.
class CustomSetting(admin.ModelAdmin):
    list_display = ('title', 'priority','created_by', 'updated_by', 'date_created', 'date_updated')
    # readonly_fields = ('created_by', 'updated_by', 'date_created', 'date_updated')  # Make fields read-only
    ordering = ('-date_created',)
    exclude = ('created_by', 'updated_by', 'date_created', 'date_updated') # Hide field when creating
    
    def save_model(self, request, obj, form, change):
        user = request.user 
        if not obj.created_by:
            obj.created_by = user
        obj.updated_by = user 
        obj.save()


admin.site.register(News, CustomSetting)