from django.core.management.base import BaseCommand
from plantas.models import Planta

class Command(BaseCommand):
    help = "Convierte todas las imágenes a formato WebP"

    def handle(self, *args, **options):
        for planta in Planta.objects.all():
            if planta.imagen and not planta.imagen.name.endswith('.webp'):
                self.stdout.write(f"Convirtiendo {planta.imagen.name}...")
                planta.save()
        self.stdout.write(self.style.SUCCESS("Conversión completada."))