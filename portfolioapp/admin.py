from django.contrib import admin
from .models import Post

# Register your models here.

#The register is used to register tables on admin so we can see them after we run the server and go to admin
#  (Post is a table registered on the admin.py)
admin.site.register(Post)
