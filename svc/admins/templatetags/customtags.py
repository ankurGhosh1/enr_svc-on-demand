from django import template
from django.db import connection


register = template.Library()


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


@register.inclusion_tag('admins/allusers.html')
def professionals():
    cursor = connection.cursor()
    cursor.execute(f'EXEC dbo.getAllProfessionals')
    professionals = dictfetchall(cursor)
    return {'professionals': professionals}