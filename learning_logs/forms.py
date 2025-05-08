from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	"""用于添加新主题的表单"""
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}  # 设置标签为空字符串

class EntryForm(forms.ModelForm):
	"""用于添加新条目的表单"""
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols':80})}