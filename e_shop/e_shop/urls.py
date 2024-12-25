from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE,name='base'),
    path('', views.HOME,name='home'),
    path('products', views.PRODUCT,name='products'),
    path('search/',views.SEARCH,name='search'),
    path('contact/',views.CONTACT_PAGE,name='contact'),
    path('products<str:id>',views.PRODUCT_DETAILS_PAGE,name='product_details'),
    path('register/',views.HANDLEREGISTER,name='register'),
    path('login/',views.HANDLELOGIN,name='login'),
    path('logout/',views.HANDLELOGOUT,name='logout'),

    #cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    path('cart/checkout/',views.Check_out,name='checkout'),

    path('cart/checkout/placeorder', views.PLACE_ORDER,name='place_order'),
    path('cart/checkout/thank_you', views.success,name='success'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
