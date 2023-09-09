
from rest_framework import serializers
import datetime

class InfoSerializer(serializers.Serializer):
    slack_name = serializers.CharField(max_length=250)
    current_day = serializers.SerializerMethodField()
    utc_time = serializers.SerializerMethodField()
    track = serializers.CharField(max_length=50)
    github_file_url = serializers.URLField()
    github_repo_url = serializers.URLField()
    status_code = serializers.IntegerField()

    def get_current_day(self, obj):
        return datetime.datetime.now().strftime('%A')
    
    def get_utc_time(self,obj):
        return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'