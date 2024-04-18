from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser


class BaseModel(models.Model):

    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractBaseUser):

    Name = models.CharField(_("Name"), max_length=100)
    Phone = models.CharField(_("Phone"), max_length=13)
    USERNAME_FIELD = "Phone"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.Name


class Post(BaseModel):
    User = models.ForeignKey(
        User, verbose_name=_("User"), related_name="user_post", on_delete=models.CASCADE
    )
    Title = models.CharField(_("Title"), max_length=200)
    Text = models.TextField(_("Text"))
    Image = models.ImageField(_("Image"), upload_to="Post/", max_length=100)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.Title


class PostComment(BaseModel):

    User = models.ForeignKey(
        User, verbose_name=_("User"), related_name="user_cm", on_delete=models.CASCADE
    )
    Post = models.ForeignKey(
        Post, verbose_name=_("Post"), related_name="post_cm", on_delete=models.CASCADE
    )
    Text = models.TextField(_(""))

    class Meta:
        verbose_name = _("PostComment")
        verbose_name_plural = _("PostComments")

    def __str__(self):
        return self.User.Name
