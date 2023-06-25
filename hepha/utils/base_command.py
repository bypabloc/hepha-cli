class BaseCommand():
    help = "Base command"

    def handle(self, *args, **options):
        raise NotImplementedError("Command must implement handle method")
