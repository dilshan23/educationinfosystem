from django.contrib import admin

#dil
from .models import Post,BlogComments
# Register your models here.
#dil
admin.site.register(Post)
admin.site.register(BlogComments)
#dil