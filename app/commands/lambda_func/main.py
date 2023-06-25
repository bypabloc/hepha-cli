from app.utils.base_command import BaseCommand


class Main(BaseCommand):
    help = 'Lambda function to get data from hephaestus'

    def handle(self, *args, **options):
        print("Hello World", args, options)
