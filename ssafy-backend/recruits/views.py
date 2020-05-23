from django.shortcuts import render, get_object_or_404
from .models import Recruit
from .serializers import RecruitCreateSerializer, RecruitDetailSerializer, RecruitSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.core.mail import EmailMessage
from django_drf_filepond.models import TemporaryUpload, StoredUpload
from django_drf_filepond.api import store_upload
from django.contrib.auth.decorators import login_required
from accouts.models import User
from portfolios.models import Tech
import os
# Create your views here.
# url = 'http://127.0.0.1:8000/media/'
@api_view(['GET'])
@permission_classes((AllowAny, )) 
def recruit_list(request):
    recruits = Recruit.objects.order_by('-pk')
    serializer = RecruitSerializer(recruits, many=True, context={'request':request,})
    return Response([serializer.data, {'recruit_count':recruits.count()}])

@api_view(['GET'])
# @login_required
def recruit_detail(request, recruit_pk):
    recruit = get_object_or_404(Recruit, pk=recruit_pk)
    serializer = RecruitDetailSerializer(recruit)
    return Response(serializer.data)


@api_view(['POST'])
# @login_required
def recruit_create(request):
    demorequest = request.data
    #######
    user = get_object_or_404(User, pk=request.data.get('user_name'))
    tech_list = []
    for tech in request.data.get('tech_category'):
        te = get_object_or_404(Tech, tech_stack=tech)
        tech_list.append(te.id)
    filepond = get_object_or_404(TemporaryUpload, upload_id=request.data.get('recruit_logo'))
    if not os.path.exists(f'./media/{user}'): #str(os.getcwd())+f'\media\{user}'
        os.makedirs(f'.\media\{user}')
    su = store_upload(filepond.upload_id, destination_file_path=f'{user}/{str(filepond.file_id)+filepond.upload_name}')
    filepond.delete()
    # http://i02b102.p.ssafy.io:8054/     http://192.168.31.126:8000/
    url = 'http://i02b102.p.ssafy.io:8054/media/' + str(su.file_path)
    if request.data.get('recruit_logo'):
        demorequest['recruit_logo'] = url
    demorequest['tech_category'] = tech_list    
    # print(demorequest)
    serializer = RecruitCreateSerializer(data=demorequest)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # print(serializer.data)
        return Response(serializer.data)
    return Response(status=400)

@api_view(['PUT','DELETE'])
# @login_required
def recruit_delete_update(request, recruit_pk):
    recruit = get_object_or_404(Recruit, pk=recruit_pk)
    demo = request.data

    if request.method == 'PUT':
        user = get_object_or_404(User, pk=request.data.get('user_name'))
        
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
        serializer = RecruitCreateSerializer(data=demo, instance=recruit)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            # return Response({'message':'update'})
    else:
        recruit.delete()
        return Response({'message':'delete'})


@api_view(['POST'])
# @login_required
def recruit_applicant(request, recruit_pk):
    recruit = get_object_or_404(Recruit, pk=recruit_pk)
    applicant_user = get_object_or_404(User, pk=request.data.get('user'))
    if recruit.applicant_user.filter(pk=applicant_user.pk).exists():
        recruit.applicant_user.remove(applicant_user.pk)
    else:
        recruit.applicant_user.add(applicant_user.pk)
        # 채용 지원하는 경우 보낼까 말까???
    serializer = RecruitDetailSerializer(recruit, context={'request':request, })
    return Response(serializer.data)


@api_view(['POST'])
# @login_required
def recruit_send_mail(request, recruit_pk):
    recruit = get_object_or_404(Recruit, pk=recruit_pk)
    demorequest = request.data
    applicant_user = get_object_or_404(User, pk=request.data.get('user'))
    template = f'''
    서버 관리자 입니다. 해당매일은 답장을 해도 반응이 없습니다.
    {recruit.title} 채용에 선정되었습니다.

    {recruit.user_name.username} 해당 메일을 통해 연락하십시오.
    '''
    emails = []
    for i in request.data:
        emails.append(i)
    mail = EmailMessage(
        f'[SSAFYedIN] 지원한 [{recruit.title}]에서 연락이 왔습니다.',
        template,
        to=emails
    )
    mail.send()
    return Response({'message':'메일보냈다.'})
