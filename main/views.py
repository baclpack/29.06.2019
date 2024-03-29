# from django.shortcuts import render

# from .models import *
# from blog.models import *
# # Create your views here.

# def orderitems_list(request):
#     orderitems = OrderItem.objects.all()
#     product_tvs = Product_TV.objects.all()
#     product_phones = Product_Phone.objects.all()
#     product_a_laptops = Product_a_laptop.objects.all()
#     context = {
#         'orderitems': orderitems,
#         'product_tvs': product_tvs,
#         'product_phones': product_phones,
#         'product_a_laptops': product_a_laptops,
#     }
#     return render(request, 'main/orderitem_list.html', context=context)





# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================


# from django.shortcuts import render
# from django.contrib import messages
# from django.shortcuts import get_object_or_404
# from django.views.generic import ListView, DetailView
# from django.shortcuts import redirect
# from django.utils import timezone

# from .models import *

# def items_list(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, "cart/item_list.html", context=context)

# class ItemDetailView(DetailView):
#     model = Item
#     template = "item_list.html"


# def add_to_cart(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     order_item, created = OrderItem.objects.get_or_create(
#         item=item,
#         user=request.user,
#         ordered=False
#     )
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item.quantity += 1
#             order_item.save()
#             messages.info(request, "This item quantity was updated.")
#             return redirect("core:product", slug=slug)
#         else:
#             order.items.add(order_item)
#             messages.info(request, "This item was added to your cart.")
#             return redirect("core:product", slug=slug)
#     else:
#         ordered_date = timezone.now()
#         order = Order.objects.create(
#             user=request.user, ordered_date=ordered_date)
#         order.items.add(order_item)
#         messages.info(request, "This item was added to your cart.")
#         return redirect("core:product", slug=slug)


# def remove_from_cart(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item = OrderItem.objects.filter(
#                 item=item,
#                 user=request.user,
#                 ordered=False
#             )[0]
#             order.items.remove(order_item)
#             messages.info(request, "This item was removed from your cart.")
#             return redirect("core:product", slug=slug)
#         else:
#             messages.info(request, "This item was not in your cart")
#             return redirect("core:product", slug=slug)
#     else:
#         messages.info(request, "You do not have an active order")
#         return redirect("core:product", slug=slug)