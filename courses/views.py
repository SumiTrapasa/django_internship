from cgitb import lookup
from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Course
from .forms import CourseModelForm
# base view class= view

class CourseObjectMixin(object):
    model=Course
    lookup = 'id'

    def get_object(self):
        id=self.kwargs.get(self.lookup)
        obj=None
        if id is not None:
            obj=get_object_or_404(self.model, id=id)
        return obj

class CourseDleteView(CourseObjectMixin,View):
    tepmlates = "courses/course_delete.html"
    
    def get(self, request, *args, **kwargs):    
        # get method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.tepmlates, context)

    def post(self, request, *args, **kwargs):   
        # post method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.tepmlates, context)



class CourseUpdateView(CourseObjectMixin,View):
    tepmlates = "courses/course_update.html"

    def get(self, request,id=None, *args, **kwargs):   
        # get method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.tepmlates, context)

    def post(self, request, id=None, *args, **kwargs):    # if self is not used then it give error no attribute META
        # post method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST ,instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.tepmlates, context)


class CourseCreateView(View):
    tepmlates = "courses/course_create.html"
    def get(self, request, *args, **kwargs):    
        form = CourseModelForm()
        # get method
        context = { "form": form}
        return render(request, self.tepmlates, context)

    def post(self, request, *args, **kwargs):    
        form = CourseModelForm(request.POST)
        # post method
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form": form}
        return render(request, self.tepmlates, context)

class CourseListView(View):
    tepmlates = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset
    

    def get(self, request, id=None, *args, **kwargs):   
        context = {'object_list':self.get_queryset()}
        return render(request, self.tepmlates, context)

class MyListView(CourseListView):
    queryset = Course.objects.filter(id=1)


class CourseView(View):
    tepmlates = "courses/course_detail.html"
    def get(self, request, id=None, *args, **kwargs):   
        # get method
        context = {}
        if id is not None:
            obj=get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.tepmlates, context)

# HTTP method
# Create your views here.
def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request,'about.html',{})