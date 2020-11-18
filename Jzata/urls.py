
from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static
from . import views
from CompanyData import views as view
from .views import Blog
from .views import resend_otp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',view.create),
    path('search',view.search,name="search"),
    path('block',view.homepage),
    path('signup',include('Emailotp.urls')),
    path('price',view.page,name="price"),
    path('',views.home,name="home"),
    path('plane',views.plane,name="plane"),
    path('gdpr',views.gdpr,name="gdpr"),
    path('privacypolicy',views.privacy,name="privacy"),
    path('service',views.service,name="service"),
    path('blog',Blog.as_view(),name="Blog"),
    path('check',view.check,name="checkProfile"),
    path('pay',views.paypal)

  
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
