# Generated by Django 2.2.4 on 2019-09-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0003_auto_20190909_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='estudantes',
            field=models.ManyToManyField(to='turmas.Estudante'),
        ),
    ]
