from rest_framework.serializers import ModelSerializer

from Faculty.models import Faculty
from Student.models import Student
from Accounts.models import UserAccount

from .models import BookmarkNotes, Note, File
class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class NoteSerializer(ModelSerializer):
    files = FileSerializer(many=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'description', 'uploaded', 'author_id', 'files']
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # def create(self, validated_data):
    #     file_data = validated_data.pop('files')
    #     note = Note.objects.create(**validated_data)
    #     for file in file_data:
    #         File.objects.create(id=note, **file_data)
    #     return note

class NoteCreateSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class BookmarkNotesSerializer(ModelSerializer):
    class Meta:
        model = BookmarkNotes
        fields = '__all__'


class NoteGenericSerializer(ModelSerializer):
    note_file = FileSerializer(many=True)
    
    class Meta:
        model = Note
        fields = ['id', 'title', 'description', 'uploaded', 'author_id', 'note_file']
    