from django.shortcuts import render

#courses views
from django.shortcuts import render
from .models import Courses
from .forms import CoursesForm
from django.shortcuts import redirect

def courses_list(request):
  courses = Courses.objects.order_by('name')
  return render(request, 'courses/courses_list.html', {'courses': courses})

def courses_new(request):
  if request.method == "POST":
    form = CoursesForm(request.POST)
    if form.is_valid():
      post = form.save(commit = False)
      post.author = request.user
      post.save()
      return redirect('/courses/view', pk = post.pk)
  else:
    form = CoursesForm()
  return render(request, 'courses/courses_edit.html', {'form': form})
