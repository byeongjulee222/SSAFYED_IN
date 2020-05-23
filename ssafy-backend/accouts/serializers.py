from rest_framework import serializers
from .models import User, Message
from portfolios.serializers import PortfolioSerializer, TechSerializer
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelChoiceField

class UserSerializer(serializers.ModelSerializer):
    portfolio_set = PortfolioSerializer(many=True)
    tech_category = TechSerializer(many=True)
    
    class Meta:
        model = User
        # fields = ('__all__',)
        depth = 1
        fields = ('id', 'email', 'username', 'password', 'portfolio_set', 'profile_img', 'verified_img', 'company','competition',
        'address', 'sns_id', 'auth', 'major', 'confirmed', 'grade', 'language', 'tech_category','nickname','recruit','is_superuser',
        'introduce', 'secession', 'email', 'award_1', 'award_2', 'award_3','applicant_competition_company','apllicant_company',)


class UserNameSerializer(serializers.ModelSerializer):
    tech_category = TechSerializer(many=True)
    class Meta:
        model = User
        fields = ('__all__')


class UserCreationSerializer(serializers.ModelSerializer):
    file = serializers.ImageField(required=False, max_length=None, use_url=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'nickname', 'grade', 'company', 'tech_category', 'verified_img', 'profile_img', 'address', 'major', 'introduce', 'award_1', 'award_2', 'award_3', 'file',)


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password',)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname', 'grade', 'company', 'major', 'address', 'award_1', 'award_2', 'award_3', 'introduce', 'tech_category', 'verified_img', 'auth', 'profile_img', )


class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'nickname', 'grade', 'company', 'award_1', 'award_2', 'award_3', 'introduce', 'tech_category', 'verified_img', 'major',)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        depth = 1
        fields = ('__all__')


class MessageSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('sender','recipient', 'content', )
