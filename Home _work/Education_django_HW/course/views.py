from django.shortcuts import render, redirect
from .models import Topic
from .forms import Topic_form


def topic_list_view(request):
    all_topics = Topic.objects.all()
    context = {"all_topics": all_topics}
    return render(request, 'topic_list_view.html', context)


def create_topic_view(request):
    if request.method == 'POST':
        form = Topic_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/topic_list')
    else:
        form = Topic_form()
    return render(request, 'create_topic.html', {'form': form})



