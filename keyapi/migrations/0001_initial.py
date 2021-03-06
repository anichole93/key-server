# Generated by Django 4.0.3 on 2022-03-21 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('imgurl', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('scheduled_date', models.DateField()),
                ('collection_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('imgurl', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='KeyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='keyapi.field')),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='keyapi.institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('imgurl', models.TextField()),
                ('description', models.TextField()),
                ('conclusions', models.TextField(blank=True)),
                ('public', models.BooleanField(default=False)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='keyapi.field')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keyapi.keyuser')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keyapi.project')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keyapi.interview')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keyapi.question')),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keyapi.project'),
        ),
        migrations.AddField(
            model_name='interview',
            name='questions',
            field=models.ManyToManyField(through='keyapi.InterviewQuestion', to='keyapi.question'),
        ),
    ]
