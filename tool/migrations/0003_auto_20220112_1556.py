# Generated by Django 3.2.6 on 2022-01-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0002_alter_task_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
