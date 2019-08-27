from blog.models import Post
from django import template

register = template.Library()
@register.inclusion_tag('blog/latest_posts.html')
def latest_posts():
	context = {
		'l_posts':Post.objects.all()[0:5],
	}
	return context
