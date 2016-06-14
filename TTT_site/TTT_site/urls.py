from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^training_evaluation/', include('training_evaluation.urls')),
	url(r'^admin/', admin.site.urls),
]