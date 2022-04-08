from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "EN"
    LANGUAGE_KOREAN = "KR"
    LANGUAGE_PERSIAN = "FR"
    LANGUAGE_TURKISH = "TR"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_TURKISH, "Turkish"),
        (LANGUAGE_PERSIAN, "Persian"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_IRR = "irr"
    CURRENCY_TRL = "trl"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_IRR, "IRR"),
        (CURRENCY_KRW, "KRW"),
        (CURRENCY_TRL, "TRL"),
    )

    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        null=True,
        blank=True,
        default=GENDER_OTHER,
    )
    bio = models.TextField(
        default="",
        blank=True,
    )
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=3,
        null=True,
        blank=True,
        default=LANGUAGE_ENGLISH,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        max_length=4,
        null=True,
        blank=True,
        default=CURRENCY_USD,
    )
    superhost = models.BooleanField(default=False)
