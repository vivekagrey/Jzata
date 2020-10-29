
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static
from . import views
from CompanyData import views as view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('32411',views.base),
    path('base',view.create),
    path('search',view.search,name="search"),
    path('',view.king)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
