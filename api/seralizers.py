from rest_framework import serializers
from univers.models import Univer, Chair, Specialization

class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ('name', 'unique_cod')

class ChairSerializers(serializers.ModelSerializer):
    specializations = SpecializationSerializers(many=True)
    class Meta:
        model = Chair
        fields = ('name', 'head_of_dep', 'teacher', 'specializations')


class UniverSerializers(serializers.ModelSerializer):
    univer_chairs = ChairSerializers(many=True)
    class Meta:
        model = Univer
        fields = ('name', 'rector', 'univer_chairs')



