from django.shortcuts import render
from .models import Post
from .models import Perros_Rescatados
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .forms import Perro_RescatadoForm
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.
def post_list(request):
    perro = Perros_Rescatados.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'perro': perro})

def post_list_user(request):
    perro = Perros_Rescatados.objects.filter(estado = "Disponible")
    return render(request, 'blog/post_list_user.html', {'perro': perro})


def inicio(request):
    perro = Perros_Rescatados.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/inicio.html',)
    if user.has_perm('blog.admin'):
        return render(request, 'blog/post_list.html', {'perro': perro}) 
    else:
        return render(request, 'blog/post_list_user.html', {'perro': perro})


def registro(request):
    return render(request, 'registration/registro.html',)

def post_detail(request, pk):
    post = get_object_or_404(Perros_Rescatados, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
        		form = Perro_RescatadoForm()
        		return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
        if request.method == "POST":
            form = Perro_RescatadoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = Perro_RescatadoForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def login(request):
    return render(request, 'registration/login.html', {})

# def post_edit(request, pk):
#         perro = get_object_or_404(Perros_Rescatados, pk=pk)
#         if request.method == "POST":
#             form = PostForm(request.POST, instance=perro)
#             if form.is_valid():
#                 perro = form.save(commit=False)
#                 perro.author = request.user
#                 perro.save()
#                 return redirect('post_detail', pk=perro.pk)
#         else:
#             form = PostForm(instance=perro)
#         return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Perros_Rescatados, pk=pk)
    if request.method == "POST":
        form = Perro_RescatadoForm(request.POST or None , request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # return redirect('detail_post_perro', pk=post.pk)
            return redirect('post_list')
    else:
        form = Perro_RescatadoForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    

def post_delete(request , pk):
    perros=Perros_Rescatados.objects.get(pk=pk)
    if request.method =="POST":
        perros.delete()
        return redirect ('post_list')
    return render(request, 'blog/post_delete.html', {'perro': perros})
