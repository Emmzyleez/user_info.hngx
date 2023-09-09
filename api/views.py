from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import InfoSerializer
import datetime

@api_view(['GET'])
def user_info_view(request):
    slack_name = request.GET.get('slack_name', 'emmanuelawobode')
    track = request.GET.get('track', 'backend')

    data = {
        'slack_name': slack_name,
        'track': track,
    }

    data['current_day'] = datetime.datetime.now().strftime('%A')
    data['utc_time'] = datetime.datetime.utcnow().replace(microsecond=0).isoformat()  + 'Z'
    data['github_file_url'] = 'https://github.com/username/repo/blob/main/file_name.ext'
    data['github_repo_url'] = 'https://github.com/username/repo'
    data['status_code'] = 200


    serializer = InfoSerializer(data=data)

    if serializer.is_valid():
        return JsonResponse(serializer.data, status=200)
    else:
        return JsonResponse(serializer.errors, status=400)

# Create your views here.
