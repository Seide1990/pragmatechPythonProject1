from django.contrib import admin

# Register your models here.
from .models import Muellimler
from .models import Fennler
from .models import sagirdler
from .models import Article

admin.site.register(Muellimler)
admin.site.register(Fennler)
admin.site.register(sagirdler)
admin.site.register(Article)