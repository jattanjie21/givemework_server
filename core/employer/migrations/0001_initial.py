# Generated by Django 3.2.15 on 2022-09-23 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization_name', models.CharField(max_length=255)),
                ('organization_contact', models.IntegerField(unique=True)),
                ('organization_email', models.EmailField(max_length=254, unique=True)),
                ('organization_address', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Employers',
            },
        ),
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hiring_manager', models.CharField(max_length=255)),
                ('hiring_manager_email', models.EmailField(max_length=254)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employer.employer')),
            ],
            options={
                'verbose_name_plural': 'Hiring',
            },
        ),
    ]
