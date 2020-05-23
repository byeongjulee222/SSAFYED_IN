from rest_framework import serializers
from .models import Recruit
from portfolios.models import Tech
from portfolios.serializers import TechSerializer
from accouts.serializers import UserNameSerializer

class RecruitSerializer(serializers.ModelSerializer):
    user_name = UserNameSerializer(read_only=True)
    tech_category = TechSerializer(read_only=True, many=True)
    class Meta:
        model = Recruit
        fields = (
            'id','user_name', 'title', 'end_date','population', 'content','condition',
            'complete','recruit_logo', 'update_at','tech_category','region','qualitificatioin',
            )


class RecruitDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruit
        depth = 2
        fields = '__all__'


class RecruitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruit
        fields = (
            'user_name','title','end_date','region','qualitificatioin','condition',
            'tech_category','content','population','company_url','recruit_logo',
            )