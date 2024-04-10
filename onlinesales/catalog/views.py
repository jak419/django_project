from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Orders, Customer, ProductSubcategory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

def index(request):
    """View function for the home page of the site."""
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    product_subcategories = ProductSubcategory.objects.annotate(total_products=Count('product'))
    
    context = {
        'product_subcategories': product_subcategories,
        'num_visits': num_visits,
    }

    if request.user.is_authenticated:
        try:
            customer = Customer.objects.get(email_address=request.user.email)
            shipped_orders = Orders.objects.filter(customer=customer, status='s').order_by('-order_date')[:5]
            context['shipped_orders'] = shipped_orders
        except Customer.DoesNotExist:
            context['shipped_orders'] = None
    # Check if user is authenticated and has the 'catalog.can_mark_shipped' permission
    if request.user.is_authenticated and request.user.has_perm('catalog.can_mark_shipped'):
        shipped_orders = Orders.objects.filter(status='s').order_by('-order_date')
        context['shipped_orders'] = shipped_orders

    return render(request, 'catalog/index.html', context)


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
    model = Orders
    template_name = 'catalog/recent_orders_list.html'
    context_object_name = 'recent_orders_list'
    paginate_by = 10  # Display 10 orders per page

    def get_queryset(self):
        # Ensure the user is authenticated and has an email
        if self.request.user.is_authenticated and self.request.user.email:
            user_email = self.request.user.email
            try:
                # Attempt to find a matching Customer based on the User's email
                customer = Customer.objects.get(email_address=user_email)
                # Filter orders by the retrieved customer and return them
                return Orders.objects.filter(customer=customer).order_by('-order_date')
            except ObjectDoesNotExist:
                # If no Customer matches, return an empty queryset
                return Orders.objects.none()
        else:
            # If the user is not authenticated or doesn't have an email, also return an empty queryset
            return Orders.objects.none()

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
    permission_required = 'catalog.can_mark_shipped'
    model = Orders
    template_name = 'catalog/shipping.html' 
    context_object_name = 'shipped_orders'

    def get_queryset(self):
        """Override to filter orders to those that have been shipped."""
        return Orders.objects.filter(status='s').order_by('-order_date')

class ShippedOrdersByUserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'catalog.can_mark_shipped'
    model = Orders
    template_name = 'catalog/shipped_orders_list_by_user.html'
    context_object_name = 'shipped_orders'

    def get_queryset(self):
        user_email = self.request.user.email
        try:
            # Attempt to find the Customer by email
            customer = Customer.objects.get(email_address=user_email)
            # Filter Orders by Customer
            return Orders.objects.filter(customer=customer, status='s').order_by('-order_date')
        except ObjectDoesNotExist:
            # If no matching Customer is found, return an empty queryset
            return Orders.objects.none()