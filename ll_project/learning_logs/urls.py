""" 定义learning_logs的URL模式 """

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
	# 主页, http://localhost:8000/
	path('', views.index, name='index'),
	# 主题列表页, http://localhost:8000/topics/
	path('topics/', views.topics, name='topics'),
	# 主题详情页, http://localhost:8000/topics/topic_id/
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	# 添加新主题, http://localhost:8000/new_topic/
	path('new_topic/', views.new_topic, name='new_topic'),
	# 在特定主题添加新条目, http://localhost:8000/new_entry/topic_id/
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]