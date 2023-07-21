from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from khoj_the_search.models import InputValue
from khoj_the_search.serializers import InputValueSerializer

class SearchView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        input_values = request.data.get('input_values')
        search_value = request.data.get('search_value')

        if not input_values or not search_value:
            return Response({"message": "Please provide input values and search value."}, status=status.HTTP_400_BAD_REQUEST)

        input_values = [int(val.strip()) for val in input_values.split(',')]
        input_values.sort(reverse=True)

        # Store the input values in the database
        input_str = ', '.join(str(val) for val in input_values)
        user_id = request.user.id if request.user.is_authenticated else None
        InputValue.objects.create(user_id=user_id, input_values=input_str)

        # Check if search value is in input values
        is_found = int(search_value) in input_values

        return Response({"result": is_found}, status=status.HTTP_200_OK)


class GetInputValues(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_datetime = request.query_params.get('start_datetime')
        end_datetime = request.query_params.get('end_datetime')
        user_id = request.query_params.get('user_id')

        if not start_datetime or not end_datetime or not user_id:
            return Response({"message": "Please provide start_datetime, end_datetime, and user_id."}, status=status.HTTP_400_BAD_REQUEST)

        input_values = InputValue.objects.filter(
            user_id=user_id,
            timestamp__gte=start_datetime,
            timestamp__lte=end_datetime
        ).order_by('-timestamp')

        serializer = InputValueSerializer(input_values, many=True)
        return Response({"status": "success", "user_id": user_id, "payload": serializer.data}, status=status.HTTP_200_OK)
