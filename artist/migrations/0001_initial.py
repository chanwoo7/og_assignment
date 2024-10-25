# Generated by Django 4.2 on 2024-10-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('M', '남성'), ('F', '여성')], max_length=10)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', '대기 중'), ('Approved', '승인됨'), ('Rejected', '반려됨')], default='Pending', max_length=10)),
                ('name', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('M', '남성'), ('F', '여성')], max_length=10)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=13)),
            ],
        ),
    ]
