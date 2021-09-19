# Generated by Django 3.2.7 on 2021-09-12 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasktrack', '0004_auto_20210608_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline_in',
            field=models.IntegerField(default=5, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasktrack.project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]