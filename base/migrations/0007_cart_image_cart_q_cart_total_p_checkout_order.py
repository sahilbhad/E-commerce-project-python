# Generated by Django 5.0.7 on 2024-12-17 10:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image',
            field=models.ImageField(default='defult.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='cart',
            name='q',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_p',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('phonenumber', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(choices=[('gujrat', 'gujrat'), ('haryana', 'haryana')], max_length=100)),
                ('zipcode', models.CharField(max_length=6)),
                ('card_num', models.CharField(max_length=16)),
                ('e_date', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=3)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=180)),
                ('price', models.IntegerField(default=0)),
                ('q', models.IntegerField(default=0)),
                ('total_p', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
