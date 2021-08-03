# posts/admin.py
from django.contrib import admin
from . models import Post
#from . models import Try


admin.site.register(Post)
# admin.site.register(Try)