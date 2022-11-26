<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
# from dataclasses import field
# import email
# from pyexpat import model
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         field = ("username", "email", "password","password2")

#     def save(self, commit = True):
#         user = super(NewUserForm, self).save(commit = False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user
