import json
from django.views.generic import DetailView, ListView, FormView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse



from .models import Category, Product
from .forms import ProductsForm



class JSONFormView(FormView):
    def get_form_kwargs(self):
        kwargs = super(JSONFormView, self).get_form_kwargs()

        if self.request.method in ('POST', 'PUT'):
            kwargs['data'] = self.request.data

        return kwargs

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


class ProductView(FormView):
    form_class = ProductsForm
    template_name = 'categories.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(data={'products':json.loads(self.request.body)})
        return kwargs

    def form_valid(self, form):
        products = Product.objects.filter(name__in=form.data['products']).values()
        return JsonResponse(list(products), safe=False)
# Create your views here.
