from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Tobacco, Cigarettes, ElecCigarettes
from accounts.models import Profile

# Create your views here.
def index(request):
    return render(request, 'cigarettes/index.html')

def like(request, tobacco_id):
    pass
    tobacco = Tobacco.objects.get(id=tobacco_id)
    try:
        user = request.user
        profile = Profile.objects.get(user=user)
    except: # 유저로그인 안했을경우
        return redirect('accounts:login')

    check_like = tobacco.like_user.filter(id=user.id)

    if check_like.exists():
        tobacco.like_user.remove(profile)
        tobacco.total_like -= 1
        tobacco.save()

    else:
        tobacco.like_user.add(profile)
        tobacco.total_like += 1
        tobacco.save()

    return redirect('tobacco:detail', tobacco_id)

def new_cigarette(request):
    tobacco_type = "cigarette"
    return render(request, 'cigarettes/create_tobacco.html', {'tobacco_type' : tobacco_type})

def new_elec_cigarette(request):
    tobacco_type = "elec_cigarette"
    return render(request, 'cigarettes/create_tobacco.html', {'tobacco_type' : tobacco_type})

def create_cigarette(request):
    cigarette = Cigarettes()
    cigarette.is_local = request.POST.get('is_local')
    cigarette.brand = request.POST.get('brand')
    cigarette.name = request.POST.get('name')
    cigarette.price = request.POST.get('price')
    cigarette.TAR = request.POST.get('tar')
    cigarette.nicotine = request.POST.get('nicotine')
    cigarette.rel_date = request.POST.get('rel_date')
    cigarette.is_menthol = request.POST.get('is_menthol')
    cigarette.save()

    #return redirect('//' +str(new_post.id))
    return redirect('cigarettes:index')

def create_elec_cigarette(request):
    elec_cigarette = ElecCigarettes()
    elec_cigarette.c_type = request.POST.get('c_type')
    elec_cigarette.brand = request.POST.get('brand')
    elec_cigarette.name = request.POST.get('name')
    elec_cigarette.price = request.POST.get('price')
    elec_cigarette.TAR = request.POST.get('tar')
    elec_cigarette.nicotine = request.POST.get('nicotine')
    elec_cigarette.rel_date = request.POST.get('rel_date')
    
    elec_cigarette.save()

    #return redirect('//' +str(new_post.id))
    return redirect('cigarettes:index')