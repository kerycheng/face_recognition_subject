# Generated by Django 2.2.5 on 2019-10-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20191019_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='Picture',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name=models.CharField(max_length=100, primary_key=True, serialize=False)),
        ),
    ]