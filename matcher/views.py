from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    if request.user.is_authenticated:
        return redirect("matcher:dashboard")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("matcher:dashboard")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def dashboard(request):
    context = {
        "applicant_name": request.user.get_full_name() or request.user.username,
    }
    return render(request, "matcher/dashboard.html", context)