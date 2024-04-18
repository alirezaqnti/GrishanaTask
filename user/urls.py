from django.urls import path
from user import views

urlpatterns = [
    path("", views.PostTemplateVew.as_view(), name="PostView"),
    path("login/", views.LoginTemplateView.as_view(), name="LoginTemplateView"),
    path("login/authentication/", views.LoginView.as_view(), name="LoginView"),
    path("post/get/<str:pk>", views.PostDet.as_view(), name="PostDet"),
    path("post/comment/new/", views.NewComment.as_view(), name="NewComment"),
    path("post/new/", views.NewPost.as_view(), name="NewPost"),
]
