from django import forms


class StudentForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    rollno=forms.IntegerField()
    feedback=forms.CharField(max_length=100,widget=forms.Textarea)
    