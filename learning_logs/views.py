from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from .utils import check_topic_owner


def index(request):
	"""学习笔记的主页"""
	return render(request, 'learning_logs/index.html')

@login_required  # 确保用户登录后才能访问主题
def topics(request):
	"""显示用户拥有的主题"""
	topics = Topic.objects.filter(owner=request.user).order_by('create_date') # 按创建日期升序排列
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	"""显示单个主题及其所有的条目"""
	topic = Topic.objects.get(id=topic_id)

	# 如果主题不属于当前用户，抛出404错误
	check_topic_owner(topic, request.user)
	
	entries = topic.entry_set.order_by('-create_date') # 减号表示降序排列
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	"""添加新主题"""
	
	if request.method != 'POST':
		# 未提交数据，创建一个新主题表单
		form = TopicForm()
	else:
		# POST提交的数据，对数据进行处理
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('learning_logs:topics')
	# 显示空表单或指出表单数据无效
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	"""在特定主题添加新条目"""
	topic = Topic.objects.get(id=topic_id)

	# 如果主题不属于当前用户，抛出404错误
	check_topic_owner(topic,request.user)
	
	if request.method != 'POST':
		# 未提交数据，创建一个新条目表单
		form = EntryForm()
	else:
		# POST提交的数据，对数据进行处理
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)  # 不保存到数据库
			new_entry.topic = topic  # 将主题与条目关联
			new_entry.save()   # 保存条目到数据库
			return redirect('learning_logs:topic', topic_id=topic_id)
		
	# 显示空表单或指出表单数据无效
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_topic(request, topic_id):
	"""编辑主题"""
	topic = Topic.objects.get(id=topic_id)

	# 如果主题不属于当前用户，抛出404错误
	check_topic_owner(topic,request.user)
	
	if request.method != 'POST':
		# 初次请求，使用当前主题填充表单
		form = TopicForm(instance=topic)
	else:
		# 使用当前主题填充表单，并根据POST提交的数据对表单进行修改
		form = TopicForm(instance=topic, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topic',topic_id=topic.id)
		
	# 显示当前表单或指出表单数据无效
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_topic.html', context)

@login_required
def edit_entry(request, entry_id):
	"""编辑条目"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	# 如果主题不属于当前用户，抛出404错误
	check_topic_owner(topic,request.user)
	
	if request.method != 'POST':
		# 初次请求，使用当前条目填充表单
		form = EntryForm(instance=entry)
	else:
		# 使用当前条目填充表单，并根据POST提交的数据对表单进行修改
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topic', topic_id=topic.id)
	# 显示当前表单或指出表单数据无效
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)
