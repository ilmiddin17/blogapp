from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', 0001_initial.py),
    ]
    operations = [
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS pg_trgm'),
    ]