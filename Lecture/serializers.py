from rest_framework.serializers import ModelSerializer

from Forum.serializers import AuthorSerializer
from .models import Lecture, Wishlist

class LectureSerializer(ModelSerializer):

    class Meta:
        model = Lecture
        fields = ['id', 'title', 'description', 'uploaded', 'author_id', 'video_firebase']

class LectureGenericSerializer(ModelSerializer):
    author_id = AuthorSerializer()

    class Meta:
        model = Lecture
        fields = ['id', 'title', 'description', 'uploaded', 'author_id', 'video_firebase']
    
    def to_representation(self, instance):
        data = super(LectureGenericSerializer, self).to_representation(instance)
        lecture_id = data['id']
        request=self.context.get("request")
        user = request.user.id

        obj=Wishlist.objects.filter(user_id=user).filter(lecture_id=lecture_id)
        if obj:
            # wishlisted  by current user
            data['wishlisted_by_user'] = 'True'
        else:
            # not wishlisted by current answer
            data['wishlisted_by_user'] = 'False'

        return data

class WishlistSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


    