from django.urls import path
from .views import BlogReviewListView, BlogReviewDetailView, BlogReviewCreateView, BlogReviewDeleteView, BlogReviewUpdateView
app_name = 'blog'

urlpatterns = [
    path('blog_reviews_list/', BlogReviewListView.as_view(), name='blog_reviews_list'),
    path('blog_review_detail/<int:pk>/', BlogReviewDetailView.as_view(), name='blog_review_detail'),
    path('blog_review_form/', BlogReviewCreateView.as_view(), name='blog_review_form'),
    path('blog_review_form/<int:pk>/update/', BlogReviewUpdateView.as_view(), name='blog_review_update'),
    path('blog_review_delete/<int:pk>/delete/', BlogReviewDeleteView.as_view(), name='blog_review_confirm_delete'),
]
