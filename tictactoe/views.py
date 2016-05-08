from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from .models import Invitation
from .forms import InvitationForm
# Create your views here.
@login_required
def new_invitation(request):
    if request.method == 'POST':
        invitation = Invitation(from_user = request.user)
        form = InvitationForm(data=request.POST, instance = invitation)
        if form.is_valid():
            form.save()
            return redirect('profiles_home')
    else:
        form = InvitationForm()

    context = {
      'form' : form
    }
    return render(request, "tictactoe/new_invitation.html", context)

@login_required
def accept_invitation(request,pk):
    invitation = get_object_or_404(Invitation, pk=pk)
    if not request.user == invitation.to_user:
        raise PermissionDenied
    if request.method == 'POST':
        if "accept" in request.POST:
            #game = Game.objects.new_game(invitation)
            invitation.delete()
            #return redirect(game.get_absolute_url())
            return HttpResponse("Invitation Accepted!")
        else:
            invitation.delete()
            return redirect('profiles_home')
    else:
        return render(request,"tictactoe/accept_invitation.html", {'invitation': invitation})