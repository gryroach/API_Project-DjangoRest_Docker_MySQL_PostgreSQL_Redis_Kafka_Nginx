from django.apps import AppConfig
# from .src.threads import CreateLogsThread


class AppLogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_logs'

    # def ready(self):
    #     print('!!!!!!!!')
    #     CreateLogsThread().start()
    #     print('Thread is run')
