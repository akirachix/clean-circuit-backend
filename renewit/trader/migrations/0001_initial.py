

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('trader', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('material', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('condition', models.CharField(max_length=50)),
                ('listed_at', models.DateTimeField()),
                ('trader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.trader')),
            ],
        ),
    ]
