# Generated by Django 3.2.2 on 2021-05-08 22:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MappingTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('entries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.mapping')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]