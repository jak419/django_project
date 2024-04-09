from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Orders, Customer, ProductSubcategory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
    """View function for the home page of the site."""
    # Example: Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    # Getting product subcategories for the sidebar
    product_subcategories = ProductSubcategory.objects.annotate(total_products=Count('product'))

    context = {
        'product_subcategories': product_subcategories,
        'num_visits': num_visits,  # Optional: add number of visits to context
    }

    return render(request, 'catalog/index.html', context=context)

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 5  # Display 5 products per page
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Get the number of visits to this view, as counted in the session variable
        num_visits = self.request.session.get('num_product_list_visits', 0)
        self.request.session['num_product_list_visits'] = num_visits + 1
        # Add number of visits to context
        context['num_visits'] = num_visits
        # Add in the product subcategories
        context['product_subcategories'] = ProductSubcategory.objects.annotate(total_products=Count('product'))
        return context

'''@login_required
def RecentOrdersView(request):
    """View function to display recent orders for the logged-in user."""
    recent_orders_list = Orders.objects.filter(customer__user=request.user).order_by('-order_date')[:10]

    context = {
        'recent_orders_list': recent_orders_list,
    }

    return render(request, 'catalog/recent_orders_list.html', context=context)'''

class RecentOrdersListView(LoginRequiredMixin, ListView):
    """Class-based view to display recent orders for the logged-in user."""
    model = Orders
    template_name = 'catalog/recent_orders_list.html'
    context_object_name = 'recent_orders_list'
    paginate_by = 10  # Displays 10 orders per page

    def get_queryset(self):
        """Override the get_queryset method to filter orders by the logged-in customer."""
        return Orders.objects.filter(customer__user=self.request.user).order_by('-order_date')

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'catalog/customer_detail.html'

class ProductSubcategoryListView(LoginRequiredMixin, ListView):
    model = ProductSubcategory
    template_name = 'catalog/product_subcategory_list.html'
    context_object_name = 'product_subcategories'

@method_decorator(login_required, name='dispatch')
def product_subcategory_view(request, subcategory_id):
    """Function-based view to display products by subcategory for logged-in users."""
    products = Product.objects.filter(product_subcategory__id=subcategory_id)
    return render(request, 'catalog/product_list_by_subcategory.html', {'products': products})

class ShippedOrdersListView(LoginRequiredMixin, ListView):
    model = Orders
    template_name = 'your_template_name_here.html'  # Specify your template name
    context_object_name = 'shipped_orders'

    def get_queryset(self):
        """Override to filter orders to those that have been shipped."""
        return Orders.objects.filter(status='s').order_by('-order_date')

class ShippedOrdersByUserListView(LoginRequiredMixin, ListView):
    """Generic class-based view listing shipped orders to current user."""
    model = Orders
    template_name = 'your_app/shipped_orders_list_by_user.html'
    context_object_name = 'shipped_orders'

    def get_queryset(self):
        """Filter orders to those that have been shipped."""
        return Orders.objects.filter(customer__user=self.request.user, status='Shipped').order_by('-order_date')