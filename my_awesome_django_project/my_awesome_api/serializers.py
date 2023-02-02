from rest_framework import serializers

from my_awesome_api.models import Person, Species


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('name', 'classification', 'language')
        representation = {'name': 'name'}


class PersonSerializer(serializers.ModelSerializer):
    species = serializers.StringRelatedField()
    
    class Meta:
        model = Person
        fields = ('name', 'birth_year', 'eye_color', 'species')
        representation = {'name': 'name'}
                