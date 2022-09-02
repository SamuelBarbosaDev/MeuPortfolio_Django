# Generated by Django 4.1 on 2022-08-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0022_contato_created_at_site_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulariodecontato',
            old_name='forma_de_contato',
            new_name='forma_de_contato_preferencial',
        ),
        migrations.RenameField(
            model_name='portfólio',
            old_name='cliente',
            new_name='nome_do_cliente',
        ),
        migrations.RemoveField(
            model_name='contato',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='formulariodecontato',
            name='data_de_publicação',
        ),
        migrations.RemoveField(
            model_name='portfólio',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='portfólio',
            name='data_de_publicação',
        ),
        migrations.RemoveField(
            model_name='site',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='sobre',
            name='created_at',
        ),
        migrations.AddField(
            model_name='contato',
            name='data_de_criação',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de criação'),
        ),
        migrations.AddField(
            model_name='formulariodecontato',
            name='data_de_criação',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de criação'),
        ),
        migrations.AddField(
            model_name='portfólio',
            name='data_de_criação',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de criação'),
        ),
        migrations.AddField(
            model_name='site',
            name='data_de_criação',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de criação'),
        ),
        migrations.AddField(
            model_name='sobre',
            name='data_de_criação',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de criação'),
        ),
    ]
