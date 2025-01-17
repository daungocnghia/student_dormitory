# Generated by Django 5.1.2 on 2024-10-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0003_deposit_confirm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=50)),
                ('rent', models.IntegerField()),
                ('electricitybill', models.IntegerField()),
                ('waterbill', models.IntegerField()),
                ('service', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='deposit',
            name='date_submit',
            field=models.CharField(max_length=100),
        ),
    ]
