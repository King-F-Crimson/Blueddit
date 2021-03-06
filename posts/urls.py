from . import views

from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('accounts/signup/', views.sign_up, name='signup'),
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('accounts/profile/<username>/', views.profile, name='profile'),
    path('accounts/update-profile/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('b/<slug:slug>/', views.CommunityView.as_view(), name='community'),
    path('posts/<int:pk>/', views.PostView.as_view(), name='post'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/update-post/<int:pk>/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('search/', views.SearchView.as_view(), name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

