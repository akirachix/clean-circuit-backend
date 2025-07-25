# Generated by Django 5.2.3 on 2025-07-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialCatalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_type', models.CharField(choices=[('cotton', 'Cotton'), ('denim', 'Denim'), ('polyester', 'Polyester'), ('linel', 'Linel'), ('satin', 'Satin'), ('silk', 'Silk'), ('wool', 'Wool')], max_length=50)),
                ('price_per_kg', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('last_update_date', models.DateField(auto_now=True)),
                ('material_description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
