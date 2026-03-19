from django.shortcuts import render, redirect

PLANTS = {
    'begonia': {
        'name': 'Begonia',
        'price': '$35.00 CAD',
        'image': 'greenhaven/images/Begonia.png',
        'size': 'Small',
        'stock': 'In Stock',
        'description': 'Begonia is a decorative indoor plant with attractive leaves and a soft elegant look.',
        'care': [
            'Bright indirect light',
            'Water when soil feels slightly dry',
            'Keep away from strong direct sun',
            'Prefers moderate humidity'
        ]
    },
    'marble-queen': {
        'name': 'Marble Queen',
        'price': '$45.00 CAD',
        'image': 'greenhaven/images/Marble Queen.png',
        'size': 'Medium',
        'stock': 'In Stock',
        'description': 'Marble Queen is a beautiful pothos variety with creamy white and green variegated leaves.',
        'care': [
            'Bright indirect light',
            'Water once top soil dries',
            'Easy to maintain',
            'Good for shelves and desks'
        ]
    },
    'calathea': {
        'name': 'Calathea',
        'price': '$78.00 CAD',
        'image': 'greenhaven/images/Calathea.png',
        'size': 'Medium',
        'stock': 'In Stock',
        'description': 'Calathea is known for its patterned foliage and adds a tropical feel indoors.',
        'care': [
            'Low to medium indirect light',
            'Keep soil slightly moist',
            'High humidity preferred',
            'Avoid direct sunlight'
        ]
    },
    'monstera-thai': {
        'name': 'Monstera Thai',
        'price': '$120.00 CAD',
        'image': 'greenhaven/images/Monstera_Thai.png',
        'size': 'Large',
        'stock': 'Not in Stock',
        'description': 'Monstera Thai has large split leaves with beautiful creamy variegation.',
        'care': [
            'Bright indirect light',
            'Water when top soil dries',
            'Support with moss pole if needed',
            'Keep in warm indoor conditions'
        ]
    },
    'pink-princess': {
        'name': 'Pink Princess',
        'price': '$150.00 CAD',
        'image': 'greenhaven/images/Pink Princess.png',
        'size': 'Medium',
        'stock': 'Limited Stock',
        'description': 'Pink Princess is a premium philodendron with stunning pink variegation.',
        'care': [
            'Bright indirect light',
            'Water moderately',
            'Use well-draining soil',
            'Avoid overwatering'
        ]
    },
    'snake-plant': {
        'name': 'Snake Plant',
        'price': '$55.00 CAD',
        'image': 'greenhaven/images/Snake Plant.png',
        'size': 'Medium',
        'stock': 'In Stock',
        'description': 'Snake Plant is a low-maintenance indoor plant perfect for beginners.',
        'care': [
            'Low to bright indirect light',
            'Water sparingly',
            'Very easy care',
            'Tolerates dry indoor air'
        ]
    },
    'string-of-hearts': {
        'name': 'String of Hearts',
        'price': '$42.00 CAD',
        'image': 'greenhaven/images/String of Hearts.png',
        'size': 'Small',
        'stock': 'In Stock',
        'description': 'String of Hearts is a trailing plant with delicate heart-shaped leaves.',
        'care': [
            'Bright indirect light',
            'Let soil dry slightly between watering',
            'Great for hanging pots',
            'Avoid soggy soil'
        ]
    },
    'verrucosum': {
        'name': 'Verrucosum',
        'price': '$95.00 CAD',
        'image': 'greenhaven/images/Verrucosum.png',
        'size': 'Medium',
        'stock': 'In Stock',
        'description': 'Verrucosum is a velvety tropical plant with rich green leaves and striking texture.',
        'care': [
            'Bright indirect light',
            'Keep humidity high',
            'Use airy soil mix',
            'Water regularly but avoid overwatering'
        ]
    },
    'monstera-albo': {
        'name': 'Monstera Albo',
        'price': '$135.00 CAD',
        'image': 'greenhaven/images/Monstera Albo.png',
        'size': 'Large',
        'stock': 'In Stock',
        'description': 'Monstera Albo is a rare premium plant with dramatic white variegation.',
        'care': [
            'Bright indirect light',
            'Water when soil partly dries',
            'Needs support as it grows',
            'Protect from harsh direct sunlight'
        ]
    },
}


def home(request):
    return render(request, 'greenhaven/home.html')


def register(request):
    return render(request, 'greenhaven/register.html')


def cart(request):
    cart_items = request.session.get('cart', [])

    total = 0
    for item in cart_items:
        price_number = float(
            item['price'].replace('$', '').replace('CAD', '').strip()
        )
        total += price_number * item['quantity']

    total_price = f"${total:.2f} CAD"

    return render(request, 'greenhaven/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def order(request):
    return render(request, 'greenhaven/order.html')


def payment(request):
    return render(request, 'greenhaven/payment.html')


def plant_details(request, plant_name):
    plant = PLANTS.get(plant_name)
    return render(request, 'greenhaven/plant_details.html', {
        'plant': plant,
        'plant_slug': plant_name
    })


def add_to_cart(request, plant_name):
    if request.method == "POST":
        plant = PLANTS.get(plant_name)

        if not plant:
            return redirect('home')

        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', [])

        found = False
        for item in cart:
            if item['slug'] == plant_name:
                item['quantity'] += quantity
                found = True
                break

        if not found:
            cart.append({
                'slug': plant_name,
                'name': plant['name'],
                'price': plant['price'],
                'image': plant['image'],
                'quantity': quantity
            })

        request.session['cart'] = cart
        request.session.modified = True

        return redirect('cart')

    return redirect('home')
def clear_cart(request):
    request.session['cart'] = []
    request.session.modified = True
    return redirect('cart')