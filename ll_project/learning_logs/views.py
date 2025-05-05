from django.shortcuts import render
from .models import Topic
# Create your views here.

def index(request):
	"""学习笔记的主页"""
	return render(request, 'learning_logs/index.html')

def topics(request):
	"""显示所有的主题"""
	topics = Topic.objects.order_by('create_date') # 升序排列
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
	"""显示单个主题及其所有的条目"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-create_date') # 减号表示降序排列
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)