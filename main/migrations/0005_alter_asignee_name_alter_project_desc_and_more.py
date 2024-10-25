# Generated by Django 4.2.16 on 2024-10-25 21:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_task_pr_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asignee",
            name="name",
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name="project",
            name="desc",
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name="project",
            name="summary",
            field=models.CharField(
                blank=True, default=None, max_length=2000, null=True
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="desc",
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name="task",
            name="summary",
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
