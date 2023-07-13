from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from jobs.views import Home

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', Home, name="Home"),
                  path('blog/', include('blog.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
