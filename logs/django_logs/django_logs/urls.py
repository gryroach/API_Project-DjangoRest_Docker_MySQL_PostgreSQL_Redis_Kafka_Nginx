from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

import sys
sys.path.append(".")

from app_logs.src.threads import CreateLogsThread

# starting logging thread
CreateLogsThread().start()
