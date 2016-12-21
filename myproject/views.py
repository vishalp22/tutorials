import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from myproject.models import Category, MainCategory
from .forms import CourseModelForm, CourseModelImage
from .models import Course_detail
from haystack.generic_views import SearchView


# Create your views here.


class WebDevelopmentDetailView(DetailView):
    model = Course_detail
    queryset = Course_detail.objects.all()
    template_name = 'web_development_single_product.html'

    def get_context_data(self, **kwargs):
        context = super(WebDevelopmentDetailView, self).get_context_data(**kwargs)
        context.update({
            'main_category': MainCategory.objects.all(),
        })
        instance = self.get_object()
        context["related"] = sorted(Course_detail.objects.get_related(instance)[:10], key=lambda x: random.random())
        return context


class CategoryListView(ListView):
    model = Category
    paginate_by = 4
    template_name = 'index.html'
    context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)

        context.update({
            'course_detail_discount_list': Course_detail.objects.order_by('-discount').distinct()[:4],
            'course_detail_recently_updated_list': Course_detail.objects.order_by('-pk').distinct()[:4],
            'course_all': Course_detail.objects.order_by('-title'),
            'main_category': MainCategory.objects.all(),
        })
        return context

    def get_queryset(self, **kwargs):
        qs = super(CategoryListView, self).get_queryset()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs


class CategoryDetailView(DetailView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'category_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context.update({
            'main_category': MainCategory.objects.all(),
        })
        obj = self.get_object()
        course_set = obj.course_detail_set.all()
        default_product = obj.default_category.all()
        courses = (course_set | default_product)
        context['courses'] = courses
        return context

    def get_queryset(self, **kwargs):
        qs = super(CategoryDetailView, self).get_queryset()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs


class CategoryTreeView(ListView):
    model = Category
    template_name = 'category_tree.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryTreeView, self).get_context_data(**kwargs)
        context.update({
            'main_category': MainCategory.objects.all(),
            'course_all': Course_detail.objects.all(),
        })
        return context


class RecentlyUpdatedList(ListView):
    model = Course_detail
    template_name = 'recently_add_list.html'

    def get_context_data(self, **kwargs):
        context = super(RecentlyUpdatedList, self).get_context_data()
        context.update({
            'recently_updated': Course_detail.objects.order_by(str('-pk')).distinct(),
            'top_discount': Course_detail.objects.order_by('-discount').distinct(),
        })
        return context

    def get_queryset(self, **kwargs):
        qs = super(RecentlyUpdatedList, self).get_queryset()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs


class TopDiscountList(ListView):
    model = Course_detail
    template_name = 'top_discount_list.html'

    def get_context_data(self, **kwargs):
        context = super(TopDiscountList, self).get_context_data()
        context.update({
            'top_discount': Course_detail.objects.order_by('-discount').distinct(),
            'recently_updated': Course_detail.objects.order_by('-pk').distinct(),
        })
        return context


@login_required
def course_model_form(request):
    title = "Course Detail Form"
    form = CourseModelForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'form.html', {"title": title, "form": form})


@login_required
def image_model_form(request):
    title = "Upload Images"
    form = CourseModelImage(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'img_form.html', {"title": title, "form": form})
