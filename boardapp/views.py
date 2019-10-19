from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import TeacherModel, ResourceModel, RatingModel, CommentModel, ProfileModel, SubjectModel, LevelModel, TopicModel, StudentModel
from .serializers import TeacherModelSerializer, ResourceModelSerializer, RatingModelSerializer, CommentModelSerializer, ProfileModelSerializer,\
    TopicModelSerializer, LevelModelSerializer, SubjectModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Count

# Create your views here.

class TeacherModelViewset(viewsets.ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherModelSerializer



class ResourceModelViewset(viewsets.ModelViewSet):
    queryset = ResourceModel.objects.all()
    serializer_class = ResourceModelSerializer

class RatingModelViewset(viewsets.ModelViewSet):
    queryset = RatingModel.objects.all()
    serializer_class = RatingModelSerializer

class CommentModelViewset(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentModelSerializer

def user_logout(request):
    logout(request)
    return JsonResponse({'OK':'Successfully logged out.'}, status=status.HTTP_200_OK)


def site_handler(request):
    if not request.user.is_authenticated:
        #return JsonResponse({'Error':'You need to authenticate first.'}, status=status.HTTP_401_UNAUTHORIZED)
        return {'Error':'You need to authenticate first'}
    try:
        r = request.user.profile
    except:
        
        #return JsonResponse({'Error':'You need to set up your profile first.'}, status=status.HTTP_401_UNAUTHORIZED)
        return {'Error':'You need to set up your profile first'}

@api_view()
def get_resources(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    if request.method =='GET':
        resources = ResourceModel.objects.filter(is_pending=False)
        serializer = ResourceModelSerializer(resources, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_teachers(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'GET':
        t_id = request.GET.get('t_id')
        if t_id:
            t_f = TeacherModel.objects.filter(id=t_id)
            if len(t_f) > 0:
                t = TeacherModel.objects.get(id=t_id)
                serializer = TeacherModelSerializer(t)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response({'Error':'No teacher with such id exists'}, status=status.HTTP_404_NOT_FOUND)
        teachers = TeacherModel.objects.all()
        serializer = TeacherModelSerializer(teachers, many = True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def get_create_resource(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    if request.method =='GET':
        rsc_id = request.GET.get('rsc_id')
        if rsc_id:
            resource_f = ResourceModel.objects.filter(id=rsc_id)
            if len(resource_f) > 0:
                resource = ResourceModel.objects.get(id=rsc_id)
                serializer = ResourceModelSerializer(resource)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response({'Error':'No resource with such id exists.'}, status=status.HTTP_404_NOT_FOUND)
        resources = ResourceModel.objects.filter(is_pending = False)
        serializer = ResourceModelSerializer(resources, many=True)
        return Response(serializer.data)




    elif request.method =='POST':
        if request.user.profile.role == 'student':
            profile = request.user.profile
            stdnt = StudentModel.objects.get(user=profile)
            disability = stdnt.disabled
            if disability:
                return Response({'Error':'You are not permitted to post.'}, status= status.HTTP_401_UNAUTHORIZED)
        serializer = ResourceModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(author=request.user.profile)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def get_create_ratings(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'GET':
        rv = request.GET.get('rsc_id')
        if rv:
            rsc_filter = ResourceModel.objects.filter(id=rv)
            if len(rsc_filter) > 0:
                rsc_obj = ResourceModel.objects.get(id=rv)
                ratings = RatingModel.objects.filter(resource = rsc_obj)
                serializer = RatingModelSerializer(ratings, many = True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'Error':'No resource with such id exists'}, status=status.HTTP_404_NOT_FOUND)
        else:
            ratings = RatingModel.objects.all()
            serializer = RatingModelSerializer(ratings, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'POST':
        serializer = RatingModelSerializer(data = request.data)
        rsc_i = request.data['resource']
        rating = request.data['rating']
        rat_f = RatingModel.objects.filter(resource=rsc_i, rator=request.user.profile)
        update = False
        if len(rat_f) > 0:
            update = True
            print('getting update')
        if serializer.is_valid():
            if update:
                rat_old = RatingModel.objects.get(resource=rsc_i, rator=request.user.profile)
                rat_old.rating = rating
                rat_old.save()
                serializer = RatingModelSerializer(rat_old)
                return Response(serializer.data,status=status.HTTP_201_CREATED)

            else:
                serializer.save(rator=request.user.profile)
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','POST'])
def get_create_comments(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'GET':
        rv = request.GET.get('rsc_id')
        rsc_filter = ResourceModel.objects.filter(id=rv)
        if len(rsc_filter) > 0:
            rsc_obj = ResourceModel.objects.get(id=rv)
            comments = CommentModel.objects.filter(resource = rsc_obj)
            serializer = CommentModelSerializer(comments, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Error':'No rsc_id found in request'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = CommentModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(commenter=request.user.profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def set_retrieve_role(request):
    if not request.user.is_authenticated:
        
        return JsonResponse({'Error':'You need to authenticate first.'}, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'GET':
        uv = request.GET.get('user_id')
        if uv:
            uf = User.objects.filter(id=uv)
            if len(uf) > 0:
                u = User.objects.get(id=uv)
                try:
                    r = u.profile
                except:
                    r = False
                if r:
                    serializer = ProfileModelSerializer(r)
                    return Response(serializer.data, status=status.HTTP_200_OK)

                else:
                    return Response({'Error':'No profile found'},status=status.HTTP_404_NOT_FOUND)
            else:
                return JsonResponse({'Error':'No User found'})
        else:
            try:
                r = request.user.profile
                
            except:
                r = False
            
            if r:
                serializer = ProfileModelSerializer(r)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'Error':'Please create a profile'}, status=status.HTTP_404_NOT_FOUND)
            
    elif request.method == 'POST':
        r = request.data['role']
        if r == 'student' or r == 'teacher':
            pass
        else:
            return Response({'Error':'Pass student or teacher as argument.'})
        pf = ProfileModel.objects.filter(user = request.user)
        if len(pf) > 0:
            return Response({"Error":"You already have a profile set up."}, status= status.HTTP_400_BAD_REQUEST)
        
        p = ProfileModel.objects.create(user = request.user, role=r)
        if r == 'student':
            StudentModel.objects.create(user=p)
        if r == 'teacher':
            TeacherModel.objects.create(user=p)
        serializer = ProfileModelSerializer(p)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def save_resource(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    rid = request.GET.get('rsc_id')
    if rid:
        rsc_f = ResourceModel.objects.filter(id=rid)
        if len(rsc_f) > 0:
            rsc = ResourceModel.objects.get(id=rid)
            rsc.saved_by.add(request.user)
            rsc.save()
            return Response({'OK':'Save successful'}, status= status.HTTP_200_OK)
        else:
            return Response({'Error':'Resource not found.'}, status = status.HTTP_404_NOT_FOUND)

    saved_r = request.user.saved_resources.all()
    serializer = ResourceModelSerializer(saved_r, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def follow_author(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    author_id = request.GET.get('aut_id')
    if author_id:
        author_f = TeacherModel.objects.filter(id=author_id)
        if len(author_f) > 0:
            author = TeacherModel.objects.get(id=author_id)
            if request.user in author.followed_by.all():
                author.followed_by.remove(request.user)
                author.save()
                return Response({"OK":"Unfollow Successful"}, status=status.HTTP_200_OK)
            author.followed_by.add(request.user)
            author.save()
            return Response({'OK':'Follow successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'Error':'No such author exists.'},status=status.HTTP_404_NOT_FOUND)
    authors = request.user.following.all()
    serializer = TeacherModelSerializer(authors, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)


stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


@api_view(['GET'])
def search(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    query = request.GET.get('q')
    if query:
        query = str(query)
        bijli = query.split(' ')
        new_bijli = []
        for bij in bijli:
            if bij in stop_words:
                pass
            else:
                new_bijli.append(bij)
        new_query = ' '.join(new_bijli)
        resources = ResourceModel.objects.filter(description__icontains=new_query)
        resources = resources.filter(is_pending = False)
        serializer = ResourceModelSerializer(resources, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    else:
        return Response({'Error':'No parameter q'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_pending(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    if request.user.profile.role == 'teacher':
        t = TeacherModel.objects.get(user = request.user.profile)
        if t.is_admin:
            resources = ResourceModel.objects.filter(is_pending = True)
            h = request.GET.get('count')
            if h:
                count = len(resources)
                return Response({'Count':count}, status = status.HTTP_200_OK)
            serializer = ResourceModelSerializer(resources, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'Not authorised. You are not teacher admin'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'Error':'Not authorised. You are not teacher admin.'}, status = status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def navigate(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    sub = request.GET.get('sub_id')
    lev = request.GET.get('lev_id')
    tpc = request.GET.get('tpc_id')
    resources = False

    if sub:
        sub_f = SubjectModel.objects.filter(id=sub)
        if len(sub_f) > 0:
            subject = SubjectModel.objects.get(id=sub)
            resources = ResourceModel.objects.filter(subject=subject, is_pending=False)
    if lev:
        lev_f = LevelModel.objects.filter(id=lev)
        if len(lev_f) > 0:
            level = LevelModel.objects.get(id=lev)
            resources = ResourceModel.objects.filter(level = level, is_pending=False)
    if tpc:
        tpc_f = TopicModel.objects.filter(id=tpc)
        if len(tpc_f) > 0:
            topic = TopicModel.objects.get(id=tpc)
            resources = ResourceModel.objects.filter(topic=topic, is_pending=False)
    if resources:
        serializer = ResourceModelSerializer(resources, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    else:
        return Response({'Error':'Please send correct ids.'}, status = status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def approve_resource(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    me = request.user.profile.role
    if me == 'teacher':
        t = TeacherModel.objects.get(user= request.user.profile)
        if t.is_admin:
            pass
        else:
            return Response({'Error':'You are not an admin.'})
    else:
        return Respone({'Error':'You are not a teacher.'})
    rsc_id = request.GET.get('rsc_id')
    if rsc_id:
        rsc_f = ResourceModel.objects.filter(id=rsc_id)
        if len(rsc_f) > 0:
            rsc = ResourceModel.objects.get(id=rsc_id)
            p = rsc.is_pending
            if p:
                rsc.is_pending = False
                rsc.save()
                return Response({'OK':'Resource is approved.'})
            else:
                return Response({'Error':'Resource already approved.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error':'No source with that id exists.'}, status = status.HTTP_404_NOT_FOUND)
    return Response({'Error':'No arguments passed.'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_topic(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    me = request.user.profile.role
    if me == 'teacher':
        t = TeacherModel.objects.get(user= request.user.profile)
        if t.is_admin:
            pass
        else:
            return Response({'Error':'You are not an admin.'})
    else:
        return Response({'Error':'You are not a teacher.'})
    
    serializer = TopicModelSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_featured(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    resources = ResourceModel.objects.filter(is_featured=True, is_pending=False).order_by('-created')[:15]
    serializer = ResourceModelSerializer(resources, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)



@api_view(['GET'])
def most_followed(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    teachers = TeacherModel.objects.annotate(num_followed_by=Count('followed_by'))
    serializer = TeacherModelSerializer(teachers, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)


    
@api_view(['GET'])
def sort_resources(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    rtng = request.GET.get('rating')
    if rtng:
        ratings = RatingModel.objects.order_by('-rating')
        resources = ResourceModel.objects.filter(id__in = ratings.values('resource_id'))
        resources = resources.filter(is_pending = False)
        serializer = ResourceModelSerializer(resources, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    resources = ResourceModel.objects.filter(is_pending=False)
    serializer = ResourceModelSerializer(resources, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)



@api_view(['GET'])
def get_topics(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    tpc_id = request.GET.get('tpc_id')
    if tpc_id:
        topic_f = TopicModel.objects.filter(id=tpc_id)
        if len(topic_f) > 0:
            topic = TopicModel.objects.get(id=tpc_id)
            serializer = TopicModelSerializer(topic)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'No topic with such id exists'}, status=status.HTTP_404_NOT_FOUND)
    
    topics = TopicModel.objects.all()
    serializer = TopicModelSerializer(topics, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_levels(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    lev_id = request.GET.get('lev_id')
    if lev_id:
        level_f = LevelModel.objects.filter(id=lev_id)
        if len(level_f) > 0:
            level = LevelModel.objects.get(id=lev_id)
            serializer = LevelModelSerializer(level)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'No level with such id exists'}, status=status.HTTP_404_NOT_FOUND)
    
    levels = LevelModel.objects.all()
    serializer = LevelModelSerializer(levels, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_subjects(request):
    msg = site_handler(request)
    if msg:
        return JsonResponse(msg,status=status.HTTP_401_UNAUTHORIZED)
    sub_id = request.GET.get('sub_id')
    if sub_id:
        subject_f = SubjectModel.objects.filter(id=sub_id)
        if len(subject_f) > 0:
            subject = SubjectModel.objects.get(id=sub_id)
            serializer = SubjectModelSerializer(subject)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'No subject with such id exists'}, status=status.HTTP_404_NOT_FOUND)
    
    subjects = SubjectModel.objects.all()
    serializer = SubjectModelSerializer(subjects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

from django.contrib.auth import login
import random, string

@api_view(['GET'])
def sign_me_in(request):
    if request.method =='GET':
        usr_id = request.GET.get('usr_id')
        if usr_id:
            usr_f = User.objects.filter(id=usr_id)
            print('lengthy: ',usr_f)
            if len(usr_f)>0:
                usr = User.objects.get(id=usr_id)
                if usr.is_active:
                    login(request, usr, backend='django.contrib.auth.backends.ModelBackend')
                    return Response({'OK':'You are logged in.'}, status=status.HTTP_200_OK)
                return Response({'Error':'User not active'}, status= status.HTTP_404_NOT_FOUND)
            else:
                username = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(15))
                email = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
                email = email + '@hotmail.com'
                usr = User.objects.create(username=username, email=email)
                login(request,usr, backend='django.contrib.auth.backends.ModelBackend')
                return Response({'OK':"New user created and you are logged in."}, status = status.HTTP_200_OK)
        return Response({'Error':"No usr_id found"}, status=status.HTTP_400_BAD_REQUEST)
    




def un(request):
    if request.user.is_authenticated:
        return JsonResponse({'OK':'You are signed in.'}, status=status.HTTP_200_OK)
    return render(request,'un.html')

def profile(request):
    print(request)
    return HttpResponse('hi')

