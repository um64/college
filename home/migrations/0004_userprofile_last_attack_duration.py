# Generated by Django 4.2.7 on 2023-12-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_userprofile_ips_delete_ipaddress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_attack_duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]