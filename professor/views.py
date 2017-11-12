#professor views
from django.shortcuts import render
from .models import ProfessorName
from .forms import ProfessorForm
from django.shortcuts import redirect

def professor_list(request):
  professors = ProfessorName.objects.order_by('name')
  return render(request, 'professor/professor_list.html', {'professors': professors})

def professor_new(request):
  if request.method == "POST":
    form = ProfessorForm(request.POST)
    if form.is_valid():
      post = form.save(commit = False)
      post.author = request.user
      post.save()
      return redirect('/professor/view', pk = post.pk)
      #return render(request, 'professor/professor_list.html', {'post' : post})
  else:
    form = ProfessorForm()
  return render(request, 'professor/professor_edit.html', {'form': form})
