from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# UserUpdateView
class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'postRequest/create_post.html'
    fields = ['username']

    def form_valid(self, form):
        form.instance.author = self.get_object().author
        return super().form_valid(form)

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False