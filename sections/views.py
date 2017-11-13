from django.shortcuts import render

#sections views
from django.shortcuts import render
from .models import Sections
from .forms import SectionsForm
from django.shortcuts import redirect

def sections_list(request):
  sections = Sections.objects.order_by('number')
  return render(request, 'sections/sections_list.html', {'sections': sections})

def sections_new(request):
  if request.method == "POST":
    form = SectionsForm(request.POST)
    if form.is_valid():
      post = form.save(commit = False)
      post.author = request.user
      post.save()
      return redirect('/sections/view', pk = post.pk)
  else:
    form = SectionsForm()
  return render(request, 'sections/sections_edit.html', {'form': form})
