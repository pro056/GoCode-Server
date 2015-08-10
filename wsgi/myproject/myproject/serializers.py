from django.forms import widgets
from rest_framework import serializers
from models import User

class userSerializer (serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('password','first_name','last_name','email_id')

class userSerializerSecure (serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name','last_name','email_id')