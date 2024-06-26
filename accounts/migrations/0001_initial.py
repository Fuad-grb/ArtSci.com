# Generated by Django 3.1.7 on 2021-03-13 23:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='media/users/user.png', upload_to='media/users/%Y/%m/%d')),
                ('bio', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=35, null=True)),
                ('linkedin', models.URLField(null=True)),
                ('facebook', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('github', models.URLField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
