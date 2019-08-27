from rest_framework import serializers
from .models import DailyReport, Checklist, AccountName, ReportImages

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
        
class DailyReportImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = ReportImages
        fields = '__all__'

# class NewOrderDetailsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = OrderDetails
#         fields = '__all__'

# class NewProductAmountsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = OrderProductAmounts
#         fields = '__all__'