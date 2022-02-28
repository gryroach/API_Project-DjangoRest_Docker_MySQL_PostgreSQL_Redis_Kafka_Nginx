from django.apps import AppConfig
# from .src.threads import thread_log


class AppLogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_logs'

    # def ready(self):
    #     print('!!!!!!!!')
    #     # thread_log()
    #     print('Thread is run')
