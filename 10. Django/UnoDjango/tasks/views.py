from django.shortcuts import render

# Create your views here.

tasks=[
    {'id': 1, 'title':'El imperio final', 'description':'primer libro'},
    {'id': 2, 'title':'El pozo de la ascensión', 'description':'segundo libro'},
    {'id': 3, 'title':'El héroe de las eras', 'description':'tercer libro'}
]

def home(request):
    context={
        'tasks':tasks
    }
    return render(request, 'tasks/home.html', context)

def task_detail(request, task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return render(request, 'tasks/task_detail.html', {'task': task})
    else:
        return render(request, 'tasks/task_not_found.html', status=404)