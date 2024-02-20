# Generated by Django 4.1.13 on 2024-02-20 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asap', '0002_resultdata_remove_iteminfo_summarized_copy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultdata',
            name='keyword',
        ),
        migrations.AddField(
            model_name='resultdata',
            name='prompt_for_background',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='resultdata',
            name='prompt_for_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
