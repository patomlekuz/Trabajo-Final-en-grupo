# Generated by Django 4.1 on 2022-09-19 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('concesionarios', '0003_post_delete_sucursal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='auto',
        ),
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posteos'),
        ),
        migrations.AddField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
