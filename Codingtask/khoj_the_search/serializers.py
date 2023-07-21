from rest_framework import serializers
from khoj_the_search.models import InputValue

class InputValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputValue
        fields = ('user', 'input_values', 'timestamp')
