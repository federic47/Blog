# Generated by Django 4.0.4 on 2022-05-25 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0006_avatar_delete_posteo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('asunto', models.CharField(max_length=50)),
                ('campo', models.CharField(max_length=50)),
            ],
        ),
    ]