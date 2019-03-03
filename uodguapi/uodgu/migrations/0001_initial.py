# Generated by Django 2.1.7 on 2019-03-03 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('tapi_key', models.CharField(blank=True, max_length=45)),
                ('tchat_id', models.CharField(blank=True, max_length=45)),
                ('dapi_key', models.CharField(blank=True, max_length=45)),
                ('dchat_id', models.CharField(blank=True, max_length=45)),
                ('soplist', models.PositiveIntegerField(default=0)),
                ('sopmanager', models.PositiveIntegerField(default=2)),
                ('guild', models.PositiveIntegerField(default=3)),
                ('champcount', models.PositiveIntegerField(default=2)),
                ('raid', models.PositiveIntegerField(default=1)),
                ('razor_key', models.CharField(blank=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('alias', models.CharField(default='', max_length=20)),
                ('rank', models.PositiveIntegerField()),
                ('roles', models.CharField(default='111', max_length=3)),
                ('email', models.CharField(default='', max_length=45)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True, null=True)),
                ('last_ip', models.CharField(blank=True, default='', max_length=11)),
                ('api_key', models.CharField(blank=True, default='', max_length=64)),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='uodgu.Guild')),
            ],
        ),
        migrations.CreateModel(
            name='Sop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField()),
                ('skill', models.CharField(default='Anatomy', max_length=20)),
                ('expiration', models.FloatField(default=0.0)),
                ('serial', models.IntegerField(default=1)),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sops', to='uodgu.Guild')),
            ],
        ),
    ]
