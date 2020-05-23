from rest_framework import serializers
from .models import Portfolio, Tech, Comment
# from accouts.serializers import UserNameSerializer
from django.conf import settings
# from accouts.models import User


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = ('id','tech_stack','portfolio_category')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        depth = 1
        fields = ('__all__')

        
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content','portfolio','user',)


class PortfolioSerializer(serializers.ModelSerializer):
    tech_category = TechSerializer(read_only=True, many=True)    
    class Meta:
        model = Portfolio
        depth = 1
        fields = ('id', 'title', 'tech_category', 'user', 'public', 'created_at', 'update_at', 'content_img_1',)

##### vue에서 수정할때 tech_category 이름까지 필요하다고 하면 updateserializer를 따로 만들어주기
##### 그전까지는 수정도 detailserializer를 통해서 사용..

class PortfolioDetailSerializer(serializers.ModelSerializer):
    tech_category = TechSerializer(many=True)
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Portfolio
        depth = 1 ## 깊이 외래키(얼마나 깊이 보여줄지정함.)
        # fields = ('id','title','tech_category', 'content_img_1', 'content_sub_1', 'content_img_2', 'content_sub_2', 'content_img_3', 'content_sub_3',
        # 'content_img_4', 'content_sub_4', 'content_img_5', 'content_sub_5', 'content_img_6', 'content_sub_6', 'content_img_7', 'content_sub_7', 'project_end','project_start',
        # 'content_img_8', 'content_sub_8', 'content_img_9', 'content_sub_9', 'content_img_10', 'content_sub_10','user', 'public', 'created_at', 'update_at','comment_set',)
        fields = ('__all__')


## tech카테고리 수정할때 숫자로 가능.
class PortfolioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('title','tech_category', 'content_img_1', 'content_sub_1', 'content_img_2', 'content_sub_2', 'content_img_3', 'content_sub_3',
        'content_img_4', 'content_sub_4', 'content_img_5', 'content_sub_5', 'content_img_6', 'content_sub_6', 'content_img_7', 'content_sub_7', 
        'content_img_8', 'content_sub_8', 'content_img_9', 'content_sub_9', 'content_img_10', 'content_sub_10', 'public','user')