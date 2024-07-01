from .models import Product, Order, OrderItem, Customer


class CartAuthenticatedUser:
    def __init__(self, request, product_id=None, action=None):
        self.request = request

        if product_id and action:
            self.add_or_delete(product_id=product_id, action=action)

    def get_cart_info(self):
        customer, created = Customer.objects.get_or_create(user=self.request.user)
        order, created = Order.objects.get_or_create(customer=customer, status=True)
        order_items = order.orderitem_set.all()

        cart_total_price = order.get_cart_total_price
        cart_total_quantity = order.get_cart_total_quantity

        return {
            'order': order,
            'order_items': order_items,
            'cart_total_price': cart_total_price,
            'cart_total_quantity': cart_total_quantity,
        }

    def add_or_delete(self, product_id, action):
        cart_info = self.get_cart_info()
        order = cart_info['order']
        product = Product.objects.get(id=product_id)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add' and product.quantity > 0:
            order_item.quantity += 1
            product.quantity -= 1

        elif action == 'delete':
            order_item.quantity -= 1
            product.quantity += 1

        order_item.save()
        product.save()

        if order_item.quantity <= 0 or action == 'h_delete':
            order_item.delete()

