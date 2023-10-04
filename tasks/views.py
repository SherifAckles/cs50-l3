from django.shortcuts import render
from django import forms


tasks=["foo","bar","baz"]

class NewTaskForm(forms.Form):
    task=forms.CharField(label="New task")
    priority= forms.IntegerField(label="Priority", min_value=1, max_value=10)



# Create your views here.
def index(request):
    return render(request, "tasks/index.html",{
        "tasks": tasks
    })
    # Add a new task:
def add(request):
    if request.method=="POST":
        #PROCESS THE RESULT OF THE REQUEST
        #a var contains all data user submitted
        form=NewTaskForm(request.POST)
        #extract clean data as a result of this form
        if form.is_valid():
            #get what task the user submitted
            task = form.cleaned_data(["task"])
            
            #add this task to the list of tasks
            tasks.append(task)
            
            #if the form isn't valid
        else:
            return render(request,"tasks/add.html",{
                #send back the existing form a new form
                "form":form
                
            })
            
            
        
        
        
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

