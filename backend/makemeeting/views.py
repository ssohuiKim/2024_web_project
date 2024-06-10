# from django.shortcuts import render


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import Meeting

# @csrf_exempt
# def create_meeting(request):
#     if request.method == 'POST':
#         try:
#             new_meeting_data = json.loads(request.body)
#             print('Received data:', new_meeting_data)  # 디버깅용 로그 추가
#             new_meeting = Meeting.objects.create(**new_meeting_data)
#             return JsonResponse({'message': 'Meeting created', 'meeting': new_meeting_data}, status=201)
#         except Exception as e:
#             print('Error:', str(e))  # 에러 로그 추가
#             return JsonResponse({'error': str(e)}, status=400)
#     elif request.method == 'GET':
#         try:
#             meetings = Meeting.objects.all().values()
#             return JsonResponse(list(meetings), safe=False, status=200)
#         except Exception as e:
#             print('Error:', str(e))  # 에러 로그 추가
#             return JsonResponse({'error': str(e)}, status=400)
#     else:
#         return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

from rest_framework import viewsets
from .models import Meeting
from .serializers import MeetingSerializer

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
