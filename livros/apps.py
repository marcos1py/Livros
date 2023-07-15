from django.apps import AppConfig


class LivrosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'livros'
    def ready(self, *args, **kwargs) -> None:
        import livros.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready