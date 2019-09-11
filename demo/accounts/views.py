from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def signin(request):
    return render(
        request,
        'accounts/signin.html',
    )


@login_required
def profile(request):
    return render(
        request,
        'accounts/profile.html',
    )
