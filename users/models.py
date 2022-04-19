import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.mail import send_mail


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
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex
            self.email_secret = secret
            send_mail(
                "Verify Airbnb account",
                f"Verify account: This is your secret {self.email_secret}",
                settings.EMAIL_HOST_USER,
                [
                    self.email,
                ],
                fail_silently=False,
            )
            self.save()
        return
