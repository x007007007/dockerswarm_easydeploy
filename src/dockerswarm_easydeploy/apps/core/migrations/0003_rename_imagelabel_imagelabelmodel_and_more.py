# Generated by Django 4.0.1 on 2022-03-26 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docker_swarm_ez_core', '0002_imagemodel_work_dir_alter_imagemodel_entrypoint'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageLabel',
            new_name='ImageLabelModel',
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='user',
            field=models.CharField(blank=True, default='root', max_length=254),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='work_dir',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='nodemodel',
            name='machine_id',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='nodemodel',
            name='manage_point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='docker_swarm_ez_core.nodemanagepointmodel'),
        ),
    ]
