# Generated by Django 4.2.5 on 2023-09-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zfunds', '0004_alter_zuser_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
