from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        form.instancewriter = self.request.user
        # 작성자의 post의 article key를 article_id에 불러온다??
        form.instance.article_id = self.request.POST.get('article_pk')
        return super().form_valid(form)

    def get_success_url(self): # 댓글 작성후에 이동하는 주소
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})

class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'
    def get_success_url(self): # 댓글 작성후에 이동하는 주소
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})
