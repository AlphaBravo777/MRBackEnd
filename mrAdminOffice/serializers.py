from rest_framework import serializers
from .models import DailyReport, Checklist, AccountName

class DailyReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyReport
        fields = '__all__'

class ChecklistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Checklist
        fields = '__all__'

class NewClientAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountName
        fields = '__all__'
        