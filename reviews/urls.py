from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.review_create, name='review_create'),
    path('<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    path('<int:review_pk>/update/', views.review_update, name='review_update'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]