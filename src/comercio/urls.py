from django.conf             import settings
from django.contrib          import admin
from django.conf.urls.static import static
from django.contrib.auth     import views as auth_views
from django.urls             import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Productos/', include('apps.productos.urls')),
    path('', views.inicio, name="inicio"),
    path('IniciarSesion/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
