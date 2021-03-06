from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from qx_base.qx_core.models import (
    ContentTypeRelated, load_set_queryset_object, ModelCountMixin
)
from qx_base.qx_user.models import QxUser, QxUser_Meta, QxUserInfo
from qx_base.qx_rest.models import RestModel, CacheModelMixin


class User(AbstractBaseUser, QxUser):
    """
    User Model
    """

    Meta = QxUser_Meta


class UserInfo(QxUserInfo):
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


def cache_func(baby):
    return baby.created.strftime('%Y%m%d')


class Baby(ContentTypeRelated, RestModel, CacheModelMixin):

    type_map_model = {
        "user": "user.User",
        "test": None,
    }
    objects_cache_fields = {
        'object': ['id', ],
        'query': ['user_id', ],
    }
    cache_config = {
        "default": {
            "BabyViewset": {
                "actions": [
                    "list",
                    "retrieve",
                ],
                'by_user_field': 'user_id',
                'async_actions': [
                    "list",
                ]
            }
        },
        "custom": {
            "BabyViewset:test_action:{}:{}": {
                "args": [
                    'id',
                    cache_func,
                ],
            },
        },
    }

    name = models.CharField(
        verbose_name="名称", default="",
        max_length=50)
    user_id = models.IntegerField(
        verbose_name="用户Id", null=True, blank=True, db_index=True)

    @staticmethod
    def load_user(queryset):
        return load_set_queryset_object(
            queryset, User, {'user_id': 'user'}, ['userinfo'])

    class Meta:
        verbose_name = 'Baby'
        verbose_name_plural = verbose_name


class Post(RestModel, ModelCountMixin):

    name = models.CharField(
        verbose_name="名称", max_length=50)
    star_count = models.PositiveIntegerField(
        verbose_name="点赞数", default=0)

    model_count_field_name = 'star_count'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = verbose_name


class TGroup(models.Model):

    name = models.CharField(
        verbose_name="名称", max_length=50)
    perms = models.ManyToManyField(
        "user.GPermission", verbose_name="权限")


class GPermission(models.Model):

    name = models.CharField(
        verbose_name="名称", max_length=50)
    groups = models.ManyToManyField(
        "user.TGroup", verbose_name="组")
