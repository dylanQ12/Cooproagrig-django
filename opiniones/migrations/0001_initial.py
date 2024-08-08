# Generated by Django 5.0.7 on 2024-08-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='img_opinions/')),
                ('nombre_completo', models.CharField(max_length=285)),
                ('comentario', models.TextField()),
            ],
        ),
    ]
