# Generated by Django 3.1 on 2020-08-15 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_modelapiview


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_basketitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages_sent', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages_received', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(django_modelapiview.JSONMixin, models.Model),
        ),
    ]