from rest_framework import generics
from rest_framework import serializers
from dockerswarm_easydeploy.apps.core.models import NodeModel, NodeGroupModel
from django.utils import timezone


class RegisterNodeSerializer(serializers.ModelSerializer):
    machine_id = serializers.CharField(max_length=254, allow_blank=True)
    docker_info = serializers.JSONField(source='node_detail', write_only=True)
    client_port = serializers.IntegerField()
    client_addr = serializers.CharField()

    class Meta:
        model = NodeModel
        fields = (
            'pk',
            'machine_id',
            'docker_info',
            'client_port',
            'client_addr',
        )

    def create(self, validated_data):
        detail = dict(validated_data)
        docker_info = validated_data['node_detail']
        detail['group'] = NodeGroupModel.objects.get_or_create(name='default')[0]
        detail['last_update_time'] = timezone.now()
        machine_id = detail.pop('machine_id')
        obj, is_created = NodeModel.objects.update_or_create(
            defaults=detail,
            machine_id=machine_id,
            uuid=docker_info['ID']
        )
        return obj


class RegisterNodeCreateOrUpdateView(generics.ListCreateAPIView):
    queryset = NodeModel.objects.all()
    serializer_class = RegisterNodeSerializer
