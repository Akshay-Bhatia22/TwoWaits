from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from .models import BookmarkNotes, File, Note
from .serializers import BookmarkNotesSerializer, NoteCreateSerializer, NoteSerializer, NoteGenericSerializer
from rest_framework.response import Response
from rest_framework import status

from Profile.UserHelpers import UserTypeHelper
def override_request(request):
    data = request.data
    data['author_id'] = request.user.id
    return data


# class NoteViewset(generics.GenericAPIView, mixins.CreateModelMixin):
#     serializer_class = NoteSerializer

#     def post(self, request, *args, **kwargs):
#         override_request(self.request)
#         for file in self.request['files']:
#             new_file = File.objects.create(id=)
#         return self.create(request, *args, **kwargs)
class NoteViewset(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = NoteSerializer

    def post(self, request, *args, **kwargs):
        override_request(request)
        return self.create(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class NoteCreate(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.GenericAPIView):

    serializer_class = NoteCreateSerializer
    permission_classes = [IsAuthenticated]
    # so that users can only update/delete their quizzes
    # queryset = Quiz.objects.filter(author_id=request)
    def get_queryset(self):
        return Note.objects.filter(author_id=self.request.user.id) 

    def post(self, request, *args, **kwargs):
        override_request(request)
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        override_request(request)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        override_request(request)
        return self.destroy(request, *args, **kwargs)

class FileAdd(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        try:
            note_instance = Note.objects.get(id=data['note_id'])
        except:
            return Response({'message':'Note object not found'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            if data['files']:
                for file in data['file']:
                    File.objects.create(note_id=note_instance, file_obj=file['file'])
                return Response({'message':'ok'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'message':'Invalid data entered'}, status=status.HTTP_406_NOT_ACCEPTABLE)


# class BookmarkNotesAdd(generics.CreateAPIView, generics.GenericAPIView):
#     serializer_class = BookmarkNotesSerializer

#     def post(self, request, *args, **kwargs):
#         override_request(request)
#         return self.create(request, *args, **kwargs)


class BookmarkNotesAdd(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        # override_request
        data['user_id'] = request.user.id
        try:
            try:
                # note already bookmarked
                existing_note = BookmarkNotes.objects.filter(user_id=data['user_id']).filter(note_id=data['note_id']).first()
                # unbookmark existing note
                existing_note.delete()
                return Response({'message':'Unbookmarked'}, status=status.HTTP_200_OK)
            except:
                # note doesn't exist
                serializer = BookmarkNotesSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                message = {'message':'Bookmarked'}
                message.update(serializer.data)
                return Response(message,status=status.HTTP_201_CREATED)
        except:
            return Response({'message':'Invalid data entered; Either user or note doesn\'t exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)


class YourBookmarkedNotes(generics.ListAPIView):
    serializer_class = NoteGenericSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Note.objects.filter(bookmark_note_id__user_id=self.request.user.id)
        return queryset
