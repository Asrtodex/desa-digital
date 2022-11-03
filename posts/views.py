from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from . models import Post
from . forms import PostCreateForm

# Create your views here.
def posts_list_view(request):
    template    = 'posts/posts_list.html'
    queryset    = get_list_or_404(Post, published = True)
    context     = {
            'objects'   : queryset
            }
    return render(request,template,context)

def posts_list_user_view(request, user):
    template    = 'posts/posts_list.html'
    queryset    = get_list_or_404(Post, published = True, user__username = user)
    context     = {
            'objects'   : queryset
            }
    return render(request,template,context)


def posts_detail_view(request, slug):
    template    = 'posts/posts_detail.html'
    instance    = get_object_or_404(Post, slug=slug) 
    context = {
            'instance'   : instance
            }
    return render(request,template,context)


# def administrator_posts_list_views(request):
#     template = 'posts/admin/posts_list.html'
#     context = {
#             'objects':'object'
#             }
#     return render(request,template,context)

def admin_posts_list_user_view(request):
    template    = 'posts/admin/posts_list.html'
    user        = request.user
    if user.username != 'admin':
        queryset    = get_list_or_404(Post, published = True, user__username = user)
    else:
        #super user can access this
        queryset    = Post.objects.all().order_by('user__username')

    context     = {
            'objects'   : queryset
            }
    return render(request,template,context)

def admin_posts_create_view(request):
    template    = 'posts/admin/posts_create.html'
    if request.method == 'POST':
        form = PostCreateForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostCreateForm()

    context = {
            'form':form,
            }
    return render(request,template,context)
