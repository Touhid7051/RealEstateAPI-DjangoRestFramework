from rest_framework import permissions,status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.response import Response
from .models import Home,ImageFiles
from .serializers import HomeSerializer,HomeDetailSerializer,ImageFilesSerializer
from django.db.models import Q


class HomeListAPIView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = HomeSerializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field = 'slug'

class HomeDetailAPIView(RetrieveAPIView):
    serializer_class = HomeDetailSerializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field = 'slug'

class ImageView(APIView):
    def get(self,request,pk,format=None):
        home=Home.objects.get(pk=pk)
        images=home.images.all()
        serializer=ImageFilesSerializer(images,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
#Multilevel/Field Search
class Search(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request,format=None):
        data=self.request.data
        queryset = Home.objects.filter(is_published=True)

        try:
            str=data['str'] #input from User 'str' is the key Normal Search
            q = (Q(description__icontains=str)) | (Q(title__icontains=str))  # Search by title and descreption fields
            queryset = queryset.filter(q)
        except:
            pass
        try:
            price_from=data['price_from'] #filter  lower range field
            queryset = queryset.filter(price__gte=price_from)
        except:
            pass
        try:
            price_to=data['price_to'] #filter upper range field
            queryset = queryset.filter(price__lte=price_to)
        except:
            pass
        try:
            city=data['city'] #filter by city
            queryset = queryset.filter(city__iexact=city)
        #gte is Greater than equal,lte is Less than Equal,iexact is Exact keyword
        except:
            pass
        serializer=HomeSerializer(queryset,many=True)
        return Response(serializer.data)