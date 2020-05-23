from rest_framework import serializers
from django.conf import settings
from .models import Competition
from portfolios.models import Tech
from portfolios.serializers import TechSerializer
from accouts.serializers import UserNameSerializer

class CompetitionsSerializer(serializers.ModelSerializer):
    ## user 시리얼라이져 생기거나 정보만 가능하면 갖고오기
    user_name = UserNameSerializer(read_only=True)
    tech_category = TechSerializer(read_only=True, many=True)
    class Meta:
        model = Competition
        fields = ('id','user_name', 'title', 'tech_category','end_date','population', 'complete','recruit_logo', 'update_at', 'created_at','content','region',)


class CompetitionDetailSerializer(serializers.ModelSerializer):
    tech_category = TechSerializer(read_only=True, many=True)
    class Meta:
        model = Competition
        depth = 2
        fields = '__all__'

class CompetitionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ('user_name','title','tech_category', 'end_date','region','qualitification','content','population','company_url','recruit_logo',)


# class TestSerializer()