# Generated by Django 3.1.2 on 2020-10-04 11:38

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('location', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('course', multiselectfield.db.fields.MultiSelectField(choices=[('PY', 'Python'), ('DJ', 'Django'), ('LI', 'Linux'), ('OR', 'Oracle')], max_length=15)),
                ('location', multiselectfield.db.fields.MultiSelectField(choices=[('ID', 'Indore'), ('SWD', 'Sendhwa'), ('HYD', 'hyderabad'), ('DH', 'Delhi')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('feedback', models.CharField(max_length=1000)),
            ],
        ),
    ]
