from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import PortfolioSerializer, TechSerializer, PortfolioDetailSerializer, PortfolioCreateSerializer, CommentSerializer, CommentCreateSerializer
from .models import Portfolio, Tech, Comment
from accouts.models import User
from pprint import pprint
from django_drf_filepond.models import TemporaryUpload
from django_drf_filepond.api import store_upload
# Create your views here.
# @api_view(['GET'])
# def index(request):

# url = 'http://127.0.0.1:8000/media/'

@api_view(['GET'])
@permission_classes((AllowAny, )) ### 권한 인증을 안받도록 해주는것 
def portfolio_list(request):
    portfolios = Portfolio.objects.filter(public=True).order_by('-pk')
    serializer = PortfolioSerializer(portfolios, many=True, context={'request':request })
    ## user 이름넣기 수정해야할듯(사용자의 실제 이름.)
    # for idx in range(len(portfolios)):
    #     serializer.data[idx]['user'] = portfolios[idx].user.username
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((AllowAny, )) ### 권한 인증을 안받도록 해주는것 
def tech(request):
    techs = Tech.objects.all()
    serializer = TechSerializer(techs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @login_required
def portfolio_detail(request, portfolio_pk):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_pk)
    # reviews = portfolio.comment_set.all()
    # print(reviews[0].content)
    serializer = PortfolioDetailSerializer(portfolio, context={'request': request,})
    # context={'request':request, 를 통해서 url 주소 가능
    return Response(serializer.data)


@api_view(['POST'])
# @login_required
def portfolio_create(request):
     # Vue랑 연결했을때 이상하면 수정 필수.
    ### 에러 작성 했을때 에러 뜨면 그때가서 바꿔주기.....
    demorequest = request.data
    # print(demorequest)
    user = get_object_or_404(User, pk=request.data.get('user'))
    for i, image in enumerate(demorequest['images']):        
        # print(image)
        # if TemporaryUpload.objects.filter(upload_id=image).exists():
        tu = get_object_or_404(TemporaryUpload, upload_id=image)
        # print(tu)
        su = store_upload(tu.upload_id, destination_file_path=f'{user}/{str(tu.file_id)+tu.upload_name}')
        tu.delete()
        # http://i02b102.p.ssafy.io:8054/media/
        url = 'http://i02b102.p.ssafy.io:8054/media/' + str(su.file_path)
        demorequest[f'content_img_{i+1}'] = url
    
    for idx, content in enumerate(demorequest['contents']):
        demorequest[f'content_sub_{idx+1}'] = content
    
    serializer = PortfolioCreateSerializer(data=demorequest)
    # print(request)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # print(serializer.data)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
# @login_required
def portfolio_delete_update(request, portfolio_pk):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_pk)
    if request.method == 'PUT':
        demorequest = request.data
        user = get_object_or_404(User, pk=portfolio.user.id)
        if demorequest.get('images'):
            for i, image in enumerate(demorequest['images']):        
                # print(image)
                if TemporaryUpload.objects.filter(upload_id=image).exists():
                    tu = get_object_or_404(TemporaryUpload, upload_id=image)
                    # print(tu)
                    su = store_upload(tu.upload_id, destination_file_path=f'{user}/{str(tu.file_id)+tu.upload_name}')
                    tu.delete()
                    # http://i02b102.p.ssafy.io:8054/media/
                    url = 'http://i02b102.p.ssafy.io:8054/media/' + str(su.file_path)
                    demorequest[f'content_img_{i+1}'] = url
        if demorequest.get('contents'):
            for idx, content in enumerate(demorequest['contents']):
                demorequest[f'content_sub_{idx+1}'] = content
        if not demorequest.get('title'):
            demorequest['title'] = portfolio.title
            demorequest['user'] = portfolio.user.id
        serializer = PortfolioCreateSerializer(data=demorequest, instance=portfolio)        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        portfolio.delete()
        return Response({'message':'deleted!'})


@api_view(['POST'])
@permission_classes((AllowAny, )) ### 권한 인증을 안받도록 해주는것 
def portfolio_page(request):
    # global page_idx
    portfolios = Portfolio.objects.filter(public=True).order_by('-pk')
    a = request.data.get('search_text','')
    # print(a)
    if a!='':
        portfolios = portfolios.filter(title__icontains=a)
    pagelen = (portfolios.count())//9+1
    # if request.data.get('page'):
    #     page_idx = int(request.data.get('page'))
    # else:
    #     page_idx = 1
    # portfolios = portfolios[9*(page_idx-1):9*page_idx]
    serializer = PortfolioSerializer(portfolios, many=True, context={'request':request })
    # pprint(serializer.data)
    return Response([serializer.data, {'pagelen':pagelen}])


@api_view(['POST'])
# @login_required
def comment_create(request, portfolio_pk):
    demo = request.data
    demo['portfolio'] = str(portfolio_pk)
    demo['user'] = str(request.data.get('user'))
    serializer = CommentCreateSerializer(data=demo)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
# @login_required
def comment_update_delete(request, portfolio_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'updated comment!!'})
    else:
        comment.delete()
        return Response({'message' : 'delete comment'})
