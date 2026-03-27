from django.db import connection
from django.db.models import Count
import django
import os

with connection.cursor() as cursor:
    cursor.execute("""
        SELECT column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_name LIKE '%user%'
        ORDER BY column_name;
    """)
    for row in cursor.fetchall():
        print(row)