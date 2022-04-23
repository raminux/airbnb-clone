import os
import requests
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.core.files.base import ContentFile
from . import forms, models


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")
    initial = {"email": "ramin.esmzad@gmail.com"}

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)

        return super().form_valid(form)


def log_gout(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        # to do: add success message
    except models.User.DoesNotExist:
        # to do: add error message
        pass

    return redirect(reverse("core:home"))


def github_login(request):
    client_id = os.environ.get("GITHUB_CLIENT_ID")
    callback_uri = "http://127.0.0.1:8000/users/login/github/callback"
    redirect_url = f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={callback_uri}&scope=read:user"
    return redirect(redirect_url)


class GithubException(Exception):
    pass


def github_callback(request):
    try:
        client_id = os.environ.get("GITHUB_CLIENT_ID")
        client_secret = os.environ.get("GITHUB_CLIENT_SECRET")
        code = request.GET.get("code", None)
        post_url = f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}"
        headers = {"Accept": "application/json"}
        if code is not None:
            response = requests.post(post_url, headers=headers)
            response_json = response.json()
            error = response_json.get("error", None)
            if error is not None:
                raise GithubException()
            else:
                oauth_token = response_json.get("access_token")
                profile_api = "https://api.github.com/user"
                profile_headers = {
                    "Accept": "application/json",
                    "Authorization": f"token {oauth_token}",
                }
                profile_response = requests.get(profile_api, headers=profile_headers)
                profile_json = profile_response.json()
                print(f"profile_json:-------------{profile_json}")
                username = profile_json.get("login", None)
                email = profile_json.get("email", None)
                avatar_url = profile_json.get("avatar_url", None)
                if username is not None and email is not None:
                    name = profile_json.get("name")
                    bio = profile_json.get("bio", None)
                    print(f"email---> {email}, name: {name}, bio: {bio}")

                    try:
                        user = models.User.objects.get(email=email)
                        if user.login_method != models.User.LOGIN_GITHUB:
                            raise GithubException()
                    except models.User.DoesNotExist:
                        user = models.User.objects.create(
                            username=email,
                            email=email,
                            bio=bio,
                            first_name=name,
                            login_method=models.User.LOGIN_GITHUB,
                            email_verified=True,
                        )
                        user.set_unusable_password()
                        user.save()
                        if avatar_url is not None:
                            avatar_request = requests.get(avatar_url)
                            print(avatar_request.content)
                            user.avatar.save(
                                f"{user}-avatar", ContentFile(avatar_request.content)
                            )

                    login(request, user)
                    return redirect(reverse("core:home"))
                else:
                    raise GithubException(
                        "Email field is empty, make it public in Github settings"
                    )
        else:
            raise GithubException()
    except GithubException:
        return redirect(reverse("users:login"))
