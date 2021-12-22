from django.views.generic import DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404

from .models import Category, Product


def paginator(qs, request, count):
    paginator = Paginator(qs, count)
    page = request.GET.get('page')
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        raise Http404("That page contains no results")
    return obj


class CategoryView(DetailView):
    model = Category
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        products = Product.objects.filter(category=self.object)
        paginator = Paginator(products, 5)
        page_number = self.request.GET.get('page')
        context['products'] = paginator.get_page(page_number)
        return context

# Create your views here.
