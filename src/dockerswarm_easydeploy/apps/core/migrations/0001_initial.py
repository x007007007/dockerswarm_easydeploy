# Generated by Django 4.0.1 on 2022-03-26 12:25

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnvNodeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='docker_swarm_ez_core.envnodemodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EvnItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_security', models.BooleanField(default=False)),
                ('default_key', models.CharField(max_length=254)),
                ('value', models.CharField(max_length=254)),
                ('node', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.envnodemodel')),
            ],
        ),
        migrations.CreateModel(
            name='ExportConfigModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_FQAN', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=254)),
                ('entrypoint', models.CharField(max_length=254)),
                ('cmds', models.JSONField(null=True)),
                ('user', models.CharField(default='root', max_length=254)),
                ('history', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageRepoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ImageSerialNodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('net_addr', models.CharField(blank=True, default='', max_length=128)),
                ('type', models.CharField(choices=[('bridge', 'bridge'), ('overlay', 'overlay'), ('ipvlan', 'ipvlan'), ('macvlan', 'macvlan')], max_length=32)),
                ('enable_ipv6', models.BooleanField(default=False)),
                ('enable_encrypted', models.BooleanField(default=False, help_text='??????overlay??????, linux only')),
                ('attachable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NodeGroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='NodeLocalNetworkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.networkmodel')),
            ],
        ),
        migrations.CreateModel(
            name='NodeManagePointModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('swarm', 'swarm'), ('standalone', 'standalone')], max_length=32)),
                ('manage_id', models.CharField(blank=True, default='', help_text='swarm ????????????id', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='NodeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(default='', max_length=64)),
                ('uuid', models.CharField(max_length=128, unique=True)),
                ('machine_id', models.CharField(max_length=254)),
                ('node_detail', models.JSONField(blank=True, null=True)),
                ('client_port', models.IntegerField(null=True)),
                ('client_addr', models.CharField(default='', max_length=254)),
                ('last_update_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_enable', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node_set', to='docker_swarm_ez_core.nodegroupmodel')),
                ('local_network_set', models.ManyToManyField(related_name='node_set', through='docker_swarm_ez_core.NodeLocalNetworkModel', to='docker_swarm_ez_core.NetworkModel')),
                ('manage_point', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='docker_swarm_ez_core.nodemanagepointmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceConfigModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=100)),
                ('service_id', models.CharField(editable=False, max_length=254)),
                ('is_stateless', models.BooleanField(default=False)),
                ('cmds', models.TextField(blank=True, default='', help_text='??????????????????,???Args')),
                ('entrypoint', models.TextField(blank=True, default='', help_text='??????')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDeployPolicyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_manager_only', models.BooleanField(default=False)),
                ('is_work_only', models.BooleanField(default=False)),
                ('is_privilege', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceExportPolicyItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.CharField(choices=[('udp', 'udp'), ('tcp', 'tcp'), ('tcp/udp', 'tcp/udp'), ('http', 'http'), ('https', 'https')], max_length=8)),
                ('is_force_https', models.BooleanField(default=True)),
                ('sni_name', models.CharField(blank=True, default='', help_text='http/https only', max_length=100)),
                ('port', models.IntegerField(default=-1, help_text='udp/tcp only')),
            ],
        ),
        migrations.CreateModel(
            name='StackConfigModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_inner', models.BooleanField(default=False)),
                ('domain_name', models.CharField(help_text='?????????????????????????????????????????????', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='VolumeClaimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('enable_instance_migration', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('volume', 'volume'), ('bind', 'bind'), ('tmp', 'tmp')], max_length=16)),
                ('src', models.CharField(blank=True, default='', help_text='????????????', max_length=254)),
                ('dst', models.CharField(max_length=254)),
                ('is_readonly', models.BooleanField(default=False)),
                ('image_serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.imageserialnodel')),
            ],
            options={
                'unique_together': {('name', 'image_serial')},
            },
        ),
        migrations.CreateModel(
            name='ServicePortConfigModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_image_cnf', models.BooleanField(default=False, editable=False)),
                ('inner_port', models.IntegerField()),
                ('export_policy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='docker_swarm_ez_core.serviceexportpolicyitemmodel')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.serviceconfigmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceNetworkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.networkmodel')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.serviceconfigmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceEnvConfigModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, help_text='???', max_length=254, null=True)),
                ('key', models.CharField(blank=True, help_text='??????????????????', max_length=254, null=True)),
                ('env_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.evnitemmodel')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.serviceconfigmodel')),
            ],
        ),
        migrations.AddField(
            model_name='serviceconfigmodel',
            name='deploy_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='docker_swarm_ez_core.servicedeploypolicymodel'),
        ),
        migrations.AddField(
            model_name='serviceconfigmodel',
            name='env_set',
            field=models.ManyToManyField(through='docker_swarm_ez_core.ServiceEnvConfigModel', to='docker_swarm_ez_core.EvnItemModel'),
        ),
        migrations.AddField(
            model_name='serviceconfigmodel',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.imageserialnodel'),
        ),
        migrations.AddField(
            model_name='serviceconfigmodel',
            name='network_set',
            field=models.ManyToManyField(through='docker_swarm_ez_core.ServiceNetworkModel', to='docker_swarm_ez_core.NetworkModel'),
        ),
        migrations.AddField(
            model_name='serviceconfigmodel',
            name='port_set',
            field=models.ManyToManyField(through='docker_swarm_ez_core.ServicePortConfigModel', to='docker_swarm_ez_core.ServiceExportPolicyItemModel'),
        ),
        migrations.AddField(
            model_name='serviceconfigmodel',
            name='stack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='docker_swarm_ez_core.stackconfigmodel'),
        ),
        migrations.AddField(
            model_name='nodelocalnetworkmodel',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.nodemodel'),
        ),
        migrations.CreateModel(
            name='ImageVolumeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=254)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.imagemodel')),
            ],
        ),
        migrations.CreateModel(
            name='ImageTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=254)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.imagemodel')),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.imagerepomodel')),
            ],
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.imageserialnodel'),
        ),
        migrations.CreateModel(
            name='ImageLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=254)),
                ('value', models.CharField(blank=True, max_length=254, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.imagemodel')),
            ],
        ),
        migrations.CreateModel(
            name='ImageExposeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField()),
                ('export_port', models.IntegerField()),
                ('protocol', models.CharField(max_length=16)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.imagemodel')),
            ],
        ),
        migrations.CreateModel(
            name='ImageEnvModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=254)),
                ('value', models.CharField(blank=True, max_length=254, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.imagemodel')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceVolumeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(default=0)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.nodemodel')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.serviceconfigmodel')),
                ('volume_claim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_swarm_ez_core.volumeclaimmodel')),
            ],
            options={
                'unique_together': {('service', 'volume_claim', 'index')},
            },
        ),
    ]
