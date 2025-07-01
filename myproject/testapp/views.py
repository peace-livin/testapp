from django.shortcuts import render
from testapp.form import StudentForm
# Create your views here.
def student_view(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            print("Name is :",form.cleaned_data["name"])
            print("Email is :",form.cleaned_data["email"])
            print("Rollno is :",form.cleaned_data["rollno"])
            print("Feedback is :",form.cleaned_data["feedback"])
            
    return render(request,"testapp/student.html",{"form":form})