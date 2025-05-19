from dataclasses import fields
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import BlogReview
from django.urls import reverse_lazy, reverse


class BlogReviewCreateView(CreateView):
    model = BlogReview
    template_name = 'blog/blog_review_form.html'
    fields = ['title', 'description', 'image', 'is_active']
    success_url = reverse_lazy('blog:blog_reviews_list')


class BlogReviewListView(ListView):
    model = BlogReview
    template_name = 'blog/blog_reviews_list.html'
    context_object_name = 'blog_reviews'

    def get_queryset(self):
        return BlogReview.objects.filter(is_active=True)


class BlogReviewDetailView(DetailView):
    model = BlogReview
    template_name = 'blog/blog_review_detail.html'
    context_object_name = 'blog_review'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.see_counter += 1
        obj.save(update_fields=['see_counter'])
        return obj


class BlogReviewUpdateView(UpdateView):
    model = BlogReview
    template_name = 'blog/blog_review_form.html'
    fields = ['title', 'description', 'image', 'is_active']
    success_url = reverse_lazy('blog:blog_review_detail')

    def get_success_url(self):
        return reverse('blog:blog_review_detail', kwargs={'pk': self.object.pk})


class BlogReviewDeleteView(DeleteView):
    model = BlogReview
    template_name = 'blog/blog_review_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_reviews_list')
    context_object_name = 'blog_review'
