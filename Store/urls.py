from django.urls import path
from Store import views 

urlpatterns=[
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name='signin'),
    path('home/',views.HomeView.as_view(),name='home'),
    path("product/<int:pk>/",views.ProductDetailView.as_view(),name="product-detail"),
    path("product/<int:pk>/carts/add/",views.AddToCartView.as_view(),name='add-to-cart'),
    path("carts/all/",views.CartItemListView.as_view(),name="cart-list"),
    path("basket/items/<int:pk>/remove/",views.BasketItemDeleteView.as_view(),name="basket-item-delete"),
    path('basket/item/<int:pk>/quantity/change/',views.BasketItemUpdateQuantityView.as_view(),name='basket-item-quantity-update'),
    path("checkout/",views.CheckOutView.as_view(),name='checkout'),
    path("myorders/all/",views.MyOrdersView.as_view(),name='myorder'),
    path("verify/",views.PaymentVerificationView.as_view(),name="verification"),
    path("signout/",views.SignOut.as_view(),name="signout"),
]