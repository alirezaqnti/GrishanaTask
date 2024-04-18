from django.conf import settings
from user.models import User


def Contexts(request):
    context = {}
    context["MEDIA_URL"] = settings.MEDIA_URL
    if "user_pk" in request.session:
        user = User.objects.get(pk=request.session["user_pk"])
        context["User"] = user
    return context
