# Generated by Django 3.0.7 on 2020-06-21 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200621_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='id',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='sno',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
