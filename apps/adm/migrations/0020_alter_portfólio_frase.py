# Generated by Django 4.1 on 2022-08-19 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0019_portfólio_frase_alter_portfólio_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfólio',
            name='frase',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
