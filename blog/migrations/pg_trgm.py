from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', <last migration filename here>),
    ]
    operations = [
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS pg_trgm'),
    ]