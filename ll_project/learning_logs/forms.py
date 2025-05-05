from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
	"""用于添加新主题的表单"""
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}  # 设置标签为空字符串