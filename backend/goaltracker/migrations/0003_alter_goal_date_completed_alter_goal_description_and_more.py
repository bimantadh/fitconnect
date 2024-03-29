# Generated by Django 5.0 on 2024-01-05 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goaltracker', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='date_completed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='goal',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='goal',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='goal',
            name='notes',
            field=models.JSONField(default={}, null=True),
        ),
        migrations.AlterField(
            model_name='goal',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('started', 'Started'), ('running', 'Running'), ('failed', 'Failed'), ('quit', 'Quit'), ('completed', 'Completed')], default='pending'),
        ),
    ]
