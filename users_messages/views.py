from django.shortcuts import render, redirect
from contact_info.models import UserMessages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def is_member(user):
    return user.groups.filter(name='manager').exists() or user.is_staff


@login_required(login_url='/login/')
@user_passes_test(is_member)
def home(request):
    messages = UserMessages.objects.filter(is_processed=False).order_by('send_date')
    paginator = Paginator(messages, 4)
    page = request.GET.get('page')
    messages = paginator.get_page((page))
    return render(request, 'messages.html', context={'items': messages})


def update_message(request, pk):
    UserMessages.objects.filter(pk=pk).update(is_processed=True)
    return redirect('/messages/#messages')
