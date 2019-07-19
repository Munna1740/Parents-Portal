# Generated by Django 2.2.1 on 2019-07-19 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admission', '0002_admission_clss'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_mark', models.IntegerField(default=0, max_length=3)),
                ('second_mark', models.IntegerField(default=0, max_length=3)),
                ('third_mark', models.IntegerField(default=0, max_length=3)),
                ('admission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.Admission')),
            ],
        ),
    ]
