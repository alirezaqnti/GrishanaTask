from rest_framework import serializers
from user.models import User, Post, PostComment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["Phone", "password"]

    def validate(self, data):
        try:
            user = User.objects.get(Phone=data["Phone"])
            if not user.check_password(data["password"]):
                raise serializers.ValidationError("incorrect Username or Password")
        except:
            raise serializers.ValidationError("incorrect Username or Password")
        return data


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostComment
        fields = ["Text", "Post", "User"]
