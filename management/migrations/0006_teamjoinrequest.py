# Generated by Django 5.1.7 on 2025-04-05 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_fix_team_college_fk'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamJoinRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.participantprofile')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_requests', to='management.team')),
            ],
        ),
    ]
