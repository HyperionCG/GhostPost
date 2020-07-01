from django.shortcuts import render, reverse, HttpResponseRedirect

from ghostapp.models import VoteChoice
from ghostapp.forms import VoteChoiceForm
# Create your views here.

def index(request):
    data = VoteChoice.objects.all()
    return render(request, 'index.html', {'data': data})

def post_view(request):
    if request.method == "POST":
        form = VoteChoiceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            VoteChoice.objects.create(
                choice=data['choice'],
                text=data['text'],
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = VoteChoiceForm()
    return render(request, 'submit_page.html', {'form': form})
    

def boast_view(request):
    data = VoteChoice.objects.filter(choice=True).order_by('-time')
    return render(request, 'index.html', {'data': data})

def roast_view(request):
    data = VoteChoice.objects.filter(choice=False).order_by('-time')
    return render(request, 'index.html', {'data': data})


def upvote_view(request, id):
    post = VoteChoice.objects.get(id=id)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def downvote_view(request, id):
    post = VoteChoice.objects.get(id=id)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def sort_view(request):
    return HttpResponseRedirect(reverse('homepage'))