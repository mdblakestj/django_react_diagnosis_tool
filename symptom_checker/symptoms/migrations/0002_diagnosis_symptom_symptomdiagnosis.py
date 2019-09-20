# Generated by Django 2.2.5 on 2019-09-14 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('symptoms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SymptomDiagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='symptoms.Diagnosis')),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='symptoms.Symptom')),
            ],
        ),
    ]
