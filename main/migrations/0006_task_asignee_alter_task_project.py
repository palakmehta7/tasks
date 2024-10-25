# Generated by Django 4.2.16 on 2024-10-25 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_alter_asignee_name_alter_project_desc_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="asignee",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="main.asignee",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="main.project"
            ),
        ),
    ]
