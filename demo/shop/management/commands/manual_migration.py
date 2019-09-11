# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
import sqlite3


class Command(BaseCommand):
    help = 'The purpose of the script is to migrate the specific app mutually'\

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str)

    def handle(self, *args, **options):
        app_name = options['app_name']
        conn = sqlite3.connect('db.sqlite3')

        res = conn.execute('select * from django_migrations').fetchall()
        self.stdout.write('migrations data:', ''.format(res))

        conn.execute('delete from django_migrations where app="{}"'.format(app_name))
        conn.commit()
        self.stdout.write('Migrate {} Manually'.format(app_name))
