from django.forms import widgets
from rest_framework import serializers
from models import User

class userSerializer (serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('name','password','phone_no','email_id')

class userSerializerSecure (serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('name','phone_no','email_id','chef_handle')