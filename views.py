from django.shortcuts import render, get_object_or_404, render_to_response,redirectfrom django.http import HttpResponse, HttpResponseRedirect,Http404from .models import Post, PostDetailfrom django.views.generic import ListView,CreateViewfrom forms import PostFormfrom django.db.models import  Qfrom django.core.exceptions import ObjectDoesNotExistfrom rest_framework.views import APIViewfrom rest_framework.response import Responsefrom rest_framework import statusfrom .serializers import PostSerializer# Create your views here.def post_list(request):    queryset = PostDetail.objects.all()    context = {        'object_list': queryset,    }    return render(request, "blog/index.html", context)class post_detail(ListView):    template_name = 'blog/view_posts.html'    def get_queryset(self):        self.postdetail = get_object_or_404(PostDetail,  slug=self.kwargs['slug'])        return Post.objects.filter(postDetail=self.postdetail)def post_create(request,):    form = PostForm(request.POST)    if form.is_valid():        instance = form.save(commit=False)        instance.save()        print instance        return redirect('blog:form_redirect')    else:        form = PostForm()        return render(request, "blog/post_form.html", {'form':form})def form_redirect(request):    return render(request,"blog/form_redirect.html",)def post_update(request, id=None):    instance = get_object_or_404(Post, id =id)    form = PostForm(request.POST or None, instance=instance)    if  form.is_valid():        instance = form.save(commit=False)        instance.save()        print instance    context = {        "title":instance.title,        "instance":instance,        "form":form,    }    return render(request, "blog/edit_post_form.html", context)def view_post(request, id=None):    try:        instance = get_object_or_404(Post, id=id)    except ObjectDoesNotExist:        return HttpResponse(status=404)    queryset = Post.objects.all()    context ={        'object_list':queryset,        'instance': instance,    }    return render(request, 'blog/view_post.html', context)def redirect_update(request):    return render(request,"blog/view_posts.html")def searchResults(request):    if request.method == 'GET':        title_name = request.GET.get('query')        if title_name:            try:                query_list = Post.objects.filter(Q(title__icontains = title_name)|                                             Q(content__icontains = title_name)                )                context = {                'object_list':query_list,            }            except ObjectDoesNotExist:                raise Http404            return render(request, 'search/search.html', context)        return HttpResponse('<h3>Enter something pusillaminous skunk!! OR go and read The Das Capital<h3>')    else:        return render(request, 'search/search.html', {})def shop(request):    render(request, 'blog/shop.html',)class PostListView(APIView):    """ List all Post details or create a new one    """    def get(self, request):        posts = Post.objects.all()        serialized = PostSerializer(posts, many=True)        return Response(serialized.data)    def post(self, request):        serializer = PostSerializer(data=request.data)        if serializer.is_valid():            serializer.save()            return Response(serializer.data, status=status.HTTP_201_CREATED)        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)class PostDetailView(APIView):    """    Get, Update or Retrieve data    """    def get_instance(self, pk):        try:            return  Post.objects.get(pk=pk)        except ObjectDoesNotExist:            raise Http404    def get(self, request, pk, format=None):        if request.method == 'GET':            post = self.get_instance(pk)            serializer = PostSerializer(post)            return Response(serializer.data)    def put(self, request, pk, format=None):        if request.method == "PUT":            post =  self.get_instance(pk)            serializer = PostSerializer(post, data=request.data)            if serializer.is_valid():                serializer.save()                return Response(serializer.data)            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    def delete(self,request, pk, format=None):        if request.method == 'DELETE':            post = self.get_instance(pk)            post.delete()            return Response(status=status.HTTP_204_NO_CONTENT)