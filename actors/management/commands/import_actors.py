import csv  # pode ser pandas
from datetime import datetime
from django.core.management.base import BaseCommand, CommandParser
from actors.models import Actor


class Command(BaseCommand):

    # se precisar de um arquivo, por exemplo
    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo com atores',
        )
        
    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))  # vai avisando os atores que ele processa

                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )
