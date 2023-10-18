# Generated by Django 4.2.6 on 2023-10-17 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('title', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='tickets/')),
                ('price', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickets.category')),
                ('tags', models.ManyToManyField(blank=True, related_name='tickets', to='tickets.tag')),
            ],
        ),
    ]