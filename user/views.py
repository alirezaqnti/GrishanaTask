from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializers import UserSerializer, PostSerializer, CommentSerializer
from user.forms import PostForm
from user.models import User, Post
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class LoginTemplateView(TemplateView):
    template_name = "Login.html"


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            us = User.objects.get(Phone=request.data["Phone"])
            refresh = RefreshToken.for_user(us)
            request.session["user_pk"] = us.pk
            token = {"refresh": str(refresh), "access": str(refresh.access_token)}
            stat = status.HTTP_200_OK
            report = "Welcome"
        else:
            report = "invalid username/password"
            stat = status.HTTP_404_NOT_FOUND
        return Response({"report": report, "token": token}, status=stat)


class PostTemplateVew(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context["Posts"] = posts
        return context


class PostDet(RetrieveAPIView):
    serializer_class = PostSerializer
    lookup_field = "pk"
    queryset = Post.objects.all()


class NewComment(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class NewPost(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            ser = PostSerializer(instance=obj)
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            print(form.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
