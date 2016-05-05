from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Invitation
from .forms import InvitationForm
# Create your views here.
@login_required
def new_invitation(request):
    if request.method == 'POST':
        form = InvitationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_home')
    else:
        form = InvitationForm()
    return render(request, "tictactoe/new_invitation.html", {'form', form})