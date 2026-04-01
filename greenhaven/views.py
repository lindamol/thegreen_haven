from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Plant, Cart, Cart_Item


def home(request):
    customer_name = request.session.get('customer_name')
    featured_plants = Plant.objects.all()[:6]

    return render(request, 'greenhaven/home.html', {
        'customer_name': customer_name,
        'featured_plants': featured_plants
    })


def register(request):
    success = False
    error = ""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not all([name, email, phone, address, username, password]):
            error = "Please fill in all fields."
        elif Customer.objects.filter(email=email).exists():
            error = "This email is already registered."
        elif Customer.objects.filter(username=username).exists():
            error = "This username is already taken."
        else:
            Customer.objects.create(
                name=name,
                email=email,
                phone=phone,
                address=address,
                username=username,
                password=password
            )
            success = True

    return render(request, 'greenhaven/register.html', {
        'success': success,
        'error': error
    })


def login_view(request):
    success = False
    error = ""

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            error = "Please enter both username and password."
        else:
            customer = Customer.objects.filter(
                username=username,
                password=password
            ).first()

            if customer:
                request.session['customer_id'] = customer.id
                request.session['customer_name'] = customer.name
                success = True
            else:
                error = "Invalid username or password."

    return render(request, 'greenhaven/login.html', {
        'success': success,
        'error': error
    })


def logout_view(request):
    request.session.flush()
    return redirect('home')


def cart(request):
    customer_id = request.session.get('customer_id')

    if not customer_id:
        return redirect('login')

    customer = get_object_or_404(Customer, id=customer_id)
    cart_obj, created = Cart.objects.get_or_create(customer=customer)

    cart_items = Cart_Item.objects.filter(cart=cart_obj).select_related('plant')

    total = 0
    for item in cart_items:
        total += float(item.plant.price) * item.quantity

    total_price = f"${total:.2f} CAD"

    return render(request, 'greenhaven/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def order_payment(request):
    return render(request, 'greenhaven/order_payment.html')


def plant_details(request, plant_name):
    plant = get_object_or_404(Plant, slug=plant_name)
    care_list = [line.strip() for line in plant.care_instructions.split('\n') if line.strip()]

    return render(request, 'greenhaven/plant_details.html', {
        'plant': plant,
        'plant_slug': plant.slug,
        'care_list': care_list
    })


def add_to_cart(request, plant_name):
    if request.method != "POST":
        return redirect('home')

    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login')

    customer = get_object_or_404(Customer, id=customer_id)
    plant = get_object_or_404(Plant, slug=plant_name)

    quantity = int(request.POST.get('quantity', 1))

    cart_obj, created = Cart.objects.get_or_create(customer=customer)

    cart_item, created = Cart_Item.objects.get_or_create(
        cart=cart_obj,
        plant=plant,
        defaults={'quantity': quantity}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    return redirect('cart')


def clear_cart(request):
    customer_id = request.session.get('customer_id')

    if not customer_id:
        return redirect('login')

    customer = get_object_or_404(Customer, id=customer_id)
    cart_obj = Cart.objects.filter(customer=customer).first()

    if cart_obj:
        Cart_Item.objects.filter(cart=cart_obj).delete()

    return redirect('cart')


def houseplants(request):
    plants = Plant.objects.all()

    return render(request, 'greenhaven/houseplants.html', {
        'plants': plants
    })


def search_plants(request):
    query = request.GET.get('q', '').strip()
    results = Plant.objects.none()

    if query:
        results = Plant.objects.filter(name__icontains=query)

    return render(request, 'greenhaven/search_results.html', {
        'query': query,
        'results': results
    })