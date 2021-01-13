# Generated by Django 3.1.3 on 2021-01-13 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210103_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.album')),
                ('review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.review')),
            ],
        ),
    ]
