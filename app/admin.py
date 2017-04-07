from django.contrib import admin
from app.models import *

# Register your models here.

class MerchantsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Merchants,MerchantsAdmin)

class ContactsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contacts,ContactsAdmin)

class BlogCategoriesAdmin(admin.ModelAdmin):
	prepopulated_fields ={ 'slug':['title'] }
admin.site.register(BlogCategories, BlogCategoriesAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    change_form_template = 'blog_editor.html'
    prepopulated_fields ={ 'slug':['title'] }
admin.site.register(BlogPost, BlogPostAdmin)

class TeamAdmin(admin.ModelAdmin):
	pass
admin.site.register(Team,TeamAdmin)

class JobCategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(JobCategories,JobCategoryAdmin)

class JobPostingAdmin(admin.ModelAdmin):
	change_form_template = 'tinymce.html'
admin.site.register(JobPosting,JobPostingAdmin)