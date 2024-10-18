from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
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
            return redirect('topic_list')
    else:
        form = Topic_form()
    return render(request, 'create_topic.html', {'form': form})


def detail_view(request, pk):
    context = get_object_or_404(Topic, pk=pk)
    return render(request, 'topic_cbv.html', context)


def topic_update(request, pk):
    context = get_object_or_404(Topic, pk=pk)
    if request.method == "POST":
        form = Topic_form(request.POST, instance=context)
        if form.is_valid():
            form.save()
            return redirect('topic_list', pk=context.pk)
    else:
        form = Topic_form(instance=context)
    return render(request, 'create_topic.html', {'form': form})


def topic_del(request, pk):
    context = get_object_or_404(Topic, pk=pk)
    if request.method == "POST":
        context.delete()
        return redirect('topic_list')
    return render(request, 'delete_topic.html', context)


