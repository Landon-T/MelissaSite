# Generated by Django 2.2.16 on 2020-10-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mel_site', '0006_auto_20201016_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('image', models.ImageField(default='null', upload_to='pictures')),
                ('url', models.CharField(max_length=1000)),
                ('tier', models.CharField(choices=[('TIER1', 'Tier 1'), ('TIER2', 'Tier 2'), ('TIER3', 'Tier 3')], default='TIER3', max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='images',
            name='category',
        ),
    ]