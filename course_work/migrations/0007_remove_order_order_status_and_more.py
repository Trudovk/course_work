# Generated by Django 4.1.9 on 2023-07-04 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_work', '0006_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_complete',
        ),
    ]