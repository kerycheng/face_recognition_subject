# Generated by Django 2.2.5 on 2019-10-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20191019_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='Picture',
            field=models.ImageField(default='', upload_to='', verbose_name=models.CharField(max_length=100, primary_key=True, serialize=False)),
        ),
    ]