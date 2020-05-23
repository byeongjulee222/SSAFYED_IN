from django.shortcuts import render, get_object_or_404
# from django.core import serializers
from django.http import HttpResponse
from .models import Competition
from accouts.models import User
from portfolios.models import Tech
from .serializers import CompetitionsSerializer, CompetitionDetailSerializer, CompetitionCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.core.mail import EmailMessage
from copy import deepcopy
from django_drf_filepond.api import store_upload, delete_stored_upload
from django_drf_filepond.models import TemporaryUpload, StoredUpload
from django.contrib.auth.decorators import login_required
import os
from subprojects.settings import BASE_DIR

# Create your views here.

@api_view(['GET'])
# JWT가 포함되어 있는지 확인
@permission_classes((AllowAny, )) ### 권한 인증을 안받도록 해주는것 
# 추후에 list함수 외에는 없애서 권한인증된 애들만 사용할 수 있도록 만들어야한다.
def competition_list(request):
    competitions = Competition.objects.order_by('-pk')
    serializer  = CompetitionsSerializer(competitions, many=True, context={'request':request,})
    # competitions.count()때문에 프론트에 설명해줘야한다.  .data[0]으로 만들어야 접근이 가능해진다.
    return Response([serializer.data, {'competition_count':competitions.count()}])


@api_view(['GET'])
# @login_required
def competition_detail(request, competition_pk):
    competition = get_object_or_404(Competition, pk=competition_pk)
    serializer = CompetitionDetailSerializer(competition, context={'request':request,})
    return Response(serializer.data)


@api_view(['POST'])
# @login_required
def competition_create(request):
    demorequest = request.data
    user = get_object_or_404(User, pk=request.data.get('user_name'))
    # demorequest['user_name'] = 1
    # user = 'aaa'
    tech_list = []
    for tech in request.data.get('tech_category'):
        te = get_object_or_404(Tech, tech_stack=tech)
        tech_list.append(te.id)
    # print(demorequest)
    # print(user)
    filepond = get_object_or_404(TemporaryUpload, upload_id=request.data.get('recruit_logo'))
    if not os.path.exists(f'./media/{user}'): #str(os.getcwd())+f'\media\{user}'
        os.makedirs(f'.\media\{user}')
    su = store_upload(filepond.upload_id, destination_file_path=f'{user}/{str(filepond.file_id)+filepond.upload_name}')
    filepond.delete()
    #http://i02b102.p.ssafy.io:8054/           http://192.168.31.126:8000/
    url = 'http://i02b102.p.ssafy.io:8054/media/' + str(su.file_path)
    demorequest['recruit_logo'] = url
    demorequest['tech_category'] = tech_list    
    serializer = CompetitionCreateSerializer(data=demorequest)
    # print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)


@api_view(['PUT','DELETE'])
# @login_required
def competition_delete_update(request, competition_pk):
    competition = get_object_or_404(Competition, pk=competition_pk)
    demo = request.data
    if request.method == 'PUT':
        user = get_object_or_404(User, pk=request.data.get('user_name'))
        
        if request.data.get('tech_category'):
            if not request.data.get('tech_category')[0].isdecimal():
                tech_list = []
                for tech in request.data.get('tech_category'):
                    te = get_object_or_404(Tech, tech_stack=tech)
                    tech_list.append(te.id)
                demo['tech_category'] = tech_list

        if len(request.data.get('recruit_logo')) < 23:
            filepond = get_object_or_404(TemporaryUpload, upload_id=request.data.get('recruit_logo'))

            su = store_upload(filepond.upload_id, destination_file_path=f'{user}/{str(filepond.file_id)+filepond.upload_name}')
            filepond.delete()
            url = 'http://i02b102.p.ssafy.io:8054/media/' + str(su.file_path)
            demo['recruit_logo'] = url
        # print(demo)
        serializer = CompetitionCreateSerializer(data=demo, instance=competition)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
            # return Response({'message':'updated competition!!!'})
    else:
        competition.delete()
        return Response(status=204)
        # return Response({'message':'deleted!!'})

# situation
# 1. 공모전에 등록하려는 유저가 버튼을 누른다. POST
# 2. 누른 유저의 아이디를 추가한다. 

@api_view(['POST'])
# @login_required
def competition_applicant(request, competition_pk):
    competition = get_object_or_404(Competition, pk=competition_pk)
    # 로그인한 유저의 번호를 받아온다   user 라는 변수로 달라고 할것.
    applicant_user = get_object_or_404(User, pk=request.data.get('user'))
    template = f'''
    서버 관리자 입니다. 해당매일은 답장을 해도 반응이 없습니다.
    {applicant_user.nickname}님이 {competition.user_name.nickname}님의 [{competition.title}] 공모전에 신청했습니다.
    지원자의 포트폴리오 페이지로 넘어 갈수 있습니다.
    http://i02b102.p.ssafy.io/profile/{applicant_user.pk}/
    '''
    if competition.applicant_competition_user.filter(pk=applicant_user.pk).exists():
        competition.applicant_competition_user.remove(applicant_user.pk)
        applicant_user.applicant_competition_company.remove(competition.pk)
    else:
        competition.applicant_competition_user.add(applicant_user.pk)
        mail = EmailMessage(
            f'[SSAFYedIN] {competition.title} 항목에서, {applicant_user.nickname}님이 지원했습니다.',
            template,
            to=[f'{competition.user_name.username}']
        )
        mail.send()
    serializer = CompetitionDetailSerializer(competition, context={'request':request,})
    return Response(serializer.data)


# competition 작성자가 신청자들한테 메일을 보낼때 사용하는 함수.
@api_view(['POST'])
# @login_required
def competition_send_mail(request, competition_pk):
    competition = get_object_or_404(Competition, pk=competition_pk)

    #### querydict에서 list로 넘어올때 .get()으로 접근하지 않고 
    # .getlist()로 접근을 해서 하나씩 가져올수 있도록 한다.
   
   
    ##### template 수정해야함.....
    template = f'''
    서버 관리자 입니다. 해당매일은 답장을 해도 반응이 없습니다.
    {competition.user_name.username}의 {competition.title}공모전 에서 함께하실수 있습니다.
    해당 메일을 통해 연락을 하십시오.
    '''
    # print(request)
    # print(request.data)
    emails = []
    for i in request.data:
        emails.append(i)
    mail = EmailMessage(
        f'[SSAFYedIN] 지원한 [{competition.title}]에서 연락이 왔습니다.',
        template,
        to=emails
    )
    # 완성이 됐을때 
    mail.send()
    serializer = CompetitionDetailSerializer(competition, context={'request':request,})
    return Response(serializer.data)


#### 아직
@api_view(['POST'])
@permission_classes((AllowAny, ))
def competiton_page(request):
    competitions = Competition.objects.order_by('-pk')
    search = request.data.get('search_text','')
    print(search)
    if search!='':
        competitions = competitions.filter(title__icontains=search)
    if request.data.get('page'):
        page_idx = int(request.data.get('page'))
    else:
        page_idx = 1
    competitions = competitions[2*(page_idx-1):2*page_idx]
    serializer = CompetitionsSerializer(competitions, many=True, context={'request':request})
    return Response(serializer.data)