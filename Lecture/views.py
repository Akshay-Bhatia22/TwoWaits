from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Lecture, Wishlist
from .serializers import LectureSerializer, LectureWishlistSerializer, LectureGenericSerializer, WishlistSerializer
from rest_framework.response import Response
from rest_framework import status

from Profile.UserHelpers import UserTypeHelper
def override_request(request):
    data = request.data
    data['author_id'] = request.user.id
    return data

# view all lectures
class LectureView(generics.ListAPIView):
    serializer_class = LectureGenericSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Lecture.objects.all()

# Create/Update/Delete view your created lectures
class LectureCreateView(generics.CreateAPIView, 
                        generics.UpdateAPIView, 
                        generics.DestroyAPIView, 
                        generics.ListAPIView):

    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated]
    # so that users can only update/delete their quizzes
    # queryset = Quiz.objects.filter(author_id=request)
    def get_queryset(self):
        return Lecture.objects.filter(author_id=self.request.user.id) 

    def post(self, request, *args, **kwargs):
        override_request(request)
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        override_request(request)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        override_request(request)
        return self.destroy(request, *args, **kwargs)


# Add to wishlist
class WishlistAdd(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        # override_request
        data['user_id'] = request.user.id
        try:
            try:
                # already wishlisted
                existing = Wishlist.objects.filter(user_id=data['user_id']).filter(lecture_id=data['lecture_id']).first()
                # unbookmark existing note
                existing.delete()
                return Response({'message':'Removed from wishlist'}, status=status.HTTP_200_OK)
            except:
                # doesn't exist
                serializer = WishlistSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                message = {'message':'added to wishlist'}
                message.update(serializer.data)
                return Response(message,status=status.HTTP_201_CREATED)
        except:
            return Response({'message':'Invalid data entered; Either user or wishlist doesn\'t exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)


class YourWishlist(generics.ListAPIView):
    serializer_class = LectureWishlistSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Lecture.objects.filter(wishlist_lecture_id__user_id=self.request.user.id)
        return queryset
