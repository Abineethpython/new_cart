from django.shortcuts import render,redirect
from . models import order,ordereditem
from product.models import product
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart = order.objects.filter(owner=customer, order_status=order.CART_STAGE).first()
    return render(request, 'cart.html', {'cart': cart})

@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=order.objects.get_or_create(
            owner=customer,
            order_status=order.CART_STAGE

        )
        products=product.objects.get(pk=product_id)
        ordered_item,created=ordereditem.objects.get_or_create(
            product=products,
            owner=cart_obj,
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity=ordered_item.quantity+quantity
            ordered_item.save()
        return redirect('cart')

def checkout_cart(request):
    try:

        if request.POST:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
            order_obj=order.objects.get(
                owner=customer,
                order_status=order.CART_STAGE

            )
            if order_obj:
                order_obj.order_status=order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                status_message="Your order is processed"
                messages.success(request,status_message)
            else:
                status_message = "Unable to processed your request"
                messages.error(request,status_message)
    except Exception as e:
        status_message = "Unable to processed your request"
        messages.error(request, status_message)
    return redirect('cart')

def remove_from_cart(request, cart_item_id):
    cart_item = ordereditem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


@login_required(login_url='account')
def show_orders(request):
    user = request.user
    customer = user.customer_profile
    all_orders=order.objects.filter(owner=customer).exclude(order_status=order.CART_STAGE)
    context={'orders':all_orders}
    return render(request, 'orders.html',context)