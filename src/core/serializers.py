from rest_framework import serializers

from .models import Post

# from django import forms


# class PostForms(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ("title", "description")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "description", "owner")
