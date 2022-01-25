from rest_framework.serializers import ModelSerializer

from Forum.serializers import AuthorSerializer
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
    author_id = AuthorSerializer()

    class Meta:
        model = Note
        fields = ['id', 'title', 'description', 'uploaded', 'author_id', 'file_obj_firebase', 'note_file']
    
    def to_representation(self, instance):
        data = super(NoteGenericSerializer, self).to_representation(instance)
        note_id = data['id']
        request=self.context.get("request")
        user = request.user.id

        obj=BookmarkNotes.objects.filter(user_id=user).filter(note_id=note_id)
        if obj:
            # bookmarked  by current user
            data['bookmarked_by_user'] = 'True'
        else:
            # not bookmarked by current answer
            data['bookmarked_by_user'] = 'False'

        return data


    