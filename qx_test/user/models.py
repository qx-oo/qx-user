from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from qx_base.qx_core.models import ContentTypeRelated
from qx_base.qx_user.models import QxUser, QxUser_Meta, QxUserInfo
from qx_base.qx_rest.models import RestCacheModel


class User(AbstractBaseUser, QxUser):
    """
    User Model
    """

    Meta = QxUser_Meta


class UserInfo(QxUserInfo, RestCacheModel):
    """
    User info
    """
    name = models.CharField(
        verbose_name="用户名称", default="",
        max_length=50)
    age = models.IntegerField(
        verbose_name="年龄")

    class Meta:
        verbose_name = 'UserInfo'
        verbose_name_plural = verbose_name


class Baby(ContentTypeRelated, RestCacheModel):

    type_map_model = {
        "user": "user.User",
        "test": None,
    }

    name = models.CharField(
        verbose_name="名称", default="",
        max_length=50)

    class Meta:
        verbose_name = 'Baby'
        verbose_name_plural = verbose_name
