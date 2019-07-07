from django.contrib.auth.models import User
import django_filters
from .models import BlogComments


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username']


class BlogFilter(django_filters.FilterSet):
	class Meta:
		model = BlogComments
		fields = ['firstname','lastname','email','comment']


