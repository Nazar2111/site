from django.urls import include, path

urlpatterns = [
    path('accounts/', include('apps.accounts.urls')),
    path('carts/', include('apps.carts.urls')),
    path('feedbacks/', include('apps.feedbacks.urls')),
    path('galleries/', include('apps.galleries.urls')),
    path('info/', include('apps.accounts.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('orders/', include('apps.orders.urls')),
    path('payments/', include('apps.payments.urls')),
    path('products/', include('apps.products.urls')),
    path('shipments/', include('apps.shipments.urls')),
    path('stats/', include('apps.stats.urls')),
    path('userprofiles/', include('apps.userprofiles.urls')),
]
