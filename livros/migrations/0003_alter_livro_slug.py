# Generated by Django 4.2.2 on 2023-06-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_alter_livro_capa_alter_livro_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
