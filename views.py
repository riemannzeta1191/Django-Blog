from django.shortcuts import render, get_object_or_404, render_to_response,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, PostDetail
from django.views import generic
from django.views.generic import ListView,CreateView
from forms import PostForm

# Create your views here.

def post_list(request):

    queryset = PostDetail.objects.all()

    context = {
        'object_list': queryset,
    }
    return render(request, "blog/index.html", context)

class post_detail(ListView):

    template_name = 'blog/view_posts.html'

    def get_queryset(self):
        self.postdetail = get_object_or_404(PostDetail,  slug=self.kwargs['slug'])
        return Post.objects.filter(postDetail=self.postdetail)


def post_create(request):
    form = PostForm(request.POST, )
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print instance
        return redirect('blog:form_redirect')
    else:
        form = PostForm()
        return render(request, "blog/post_form.html", {'form':form})

def form_redirect(request):

  return render(request,"blog/form_redirect.html",)


#
# class post_create(CreateView):
#     model = Post
#     fields = ['title', 'content', 'postDetail']

