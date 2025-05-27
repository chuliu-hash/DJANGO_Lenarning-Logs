from django.http import Http404

def check_topic_owner(topic, user):
	"""检查主题是否属于特定用户"""
	if topic.owner != user:
		raise Http404("You do not have permission to access this topic.")