from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Category, LikeDislike, YearPeriod, Language, View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, BookSearchForm


def books_list(request):
    products = Product.objects.all()
    return render(request, 'books_list.html', {'products': products})


def books(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'languages': Language.objects.all(),
        'year_periods': YearPeriod.objects.all(),
    }
    return render(request, 'books.html', context)


def books_by_language(request, language_slug):
    language = Language.objects.get(slug=language_slug)
    products = Product.objects.filter(language=language)
    context = {
        'products': products,
        'languages': Language.objects.all(),
        'year_periods': YearPeriod.objects.all(),

    }
    return render(request, 'books.html', context)


def books_by_year(request, year_slug):
    year = YearPeriod.objects.get(slug=year_slug)
    products = Product.objects.filter(year_period=year)
    context = {
        'products': products,
        'languages': Language.objects.all(),
        'year_periods': YearPeriod.objects.all(),

    }
    return render(request, 'books.html', context)


def books_by_date(request):
    products = Product.objects.order_by('-added')
    context = {
        'products': products,
        'languages': Language.objects.all(),
        'year_periods': YearPeriod.objects.all(),

    }
    return render(request, 'books.html', context)


def books_by_rating(request):
    products = Product.objects.order_by('-rating')
    context = {
        'products': products,
        'languages': Language.objects.all(),
        'year_periods': YearPeriod.objects.all(),

    }
    return render(request, 'books.html', context)


def books_by_popularity(request):
    products = Product.objects.order_by('-views')
    context = {
        'products': products,
        'languages': Language.objects.all(),
        'year_periods': YearPeriod.objects.all(),

    }
    return render(request, 'books.html', context)


def books_in_page(request, number):
    products = Product.objects.all()[:number]
    context = {
        'products': products,
        'languages': Language.objects.all(),
        'year_periods': YearPeriod.objects.all(),

    }
    return render(request, 'books.html', context)


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        # Did they fill out the form
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            # Is the form valid
            if form.is_valid():
                form.save()
                messages.success(request, "Your Password Has Been Updated...")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form': form})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "User Has Been Updated!!")
            return redirect('home')
        return render(request, "update_user.html", {'user_form': user_form})
    else:
        messages.success(request, "You Must Be Logged In To Access That Page!!")
        return redirect('home')


def category_summary(request):
    return render(request, 'category_summary.html', {})


def category(request, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, {"That Category doesn't exist!"})
        return redirect('home')


def product(request, pk):
    product = Product.objects.get(id=pk)
    user_has_viewed = View.objects.filter(user=request.user, product=product).exists()

    if not user_has_viewed:
        product.views += 1
        product.save()

        View.objects.create(user=request.user, product=product)
    return render(request, 'product.html', {"product": product})


def home(request):
    products = Product.objects.order_by('-pk')[:4]
    products_by_rating = Product.objects.order_by('-rating')[:8]

    context = {
        'products': products,
        'products_by_rating': products_by_rating
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.success(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have Register Successfully! Welcome!')
            return redirect('home')
        else:
            messages.error(request, 'Whooops! There was a problem Registering, plaese try again')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})



@login_required
def toggle_like(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    like_dislike, created = LikeDislike.objects.get_or_create(user=request.user, product=product)
    if not created:
        like_dislike.delete()
    return redirect('home')


def liked_products(request, user_id):
    user = User.objects.get(id=user_id)
    likes = LikeDislike.objects.filter(user=user)
    return render(request, 'liked_products.html', {'likes': likes})


def search_books(request):
    query = ""
    results = []

    if 'query' in request.GET:
        form = BookSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Perform the search
            results = Product.objects.filter(title__icontains=query)
    else:
        form = BookSearchForm()

    return render(request, 'books.html', {'form': form, 'products': results})
