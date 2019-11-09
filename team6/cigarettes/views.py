from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from cigarettes.models import Tobacco, Cigarettes, ElecCigarettes, Comment 
from accounts.models import Profile

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        tobacco = Tobacco.objects.all()
        context = {'tobacco':tobacco}
        return render(request, 'cigarettes/index.html', context)    
    else:
        tobacco = Tobacco.objects.all()
        user = request.user
        profile = Profile.objects.get(user = user)
        context = {'tobacco':tobacco, 'profile':profile}
        return render(request, 'cigarettes/index.html', context)

def detail(request, cigarette_id):
    tobacco = get_object_or_404(Tobacco, pk = cigarette_id)
    comment_list = Comment.objects.filter(belongs_to_tobacco=tobacco)

    foh_dict = {'상':0,'중':0,'하':0}
    score = 0

    if not len(comment_list) == 0:
        for comment in comment_list:
            score += comment.score 
            if comment.feel_of_hit == '상':
                foh_dict['상'] += 1
            elif comment.feel_of_hit == '중':
                foh_dict['중'] += 1
            else:
                foh_dict['하'] += 1
        
        tobacco.score = score / len(comment_list)

        if (foh_dict['상'] > foh_dict['중']) and (foh_dict['상'] > foh_dict['하']):
            tobacco.feel_of_hit = '상'
        elif (foh_dict['하'] > foh_dict['중']) and (foh_dict['하'] > foh_dict['상']):
            tobacco.feel_of_hit = '하'
        else: tobacco.feel_of_hit = '중'

    tobacco.save()

    context = {
        'tobacco':tobacco,
        'comment_list':comment_list,
    }
    
    return render(request,"cigarettes/cigarette_detail.html", context)

def like(request, cigarette_id):

    tobacco = Tobacco.objects.get(id=cigarette_id)
    try:
        user = request.user
        profile = Profile.objects.get(user=user)
    except: # 유저로그인 안했을경우
        return redirect('accounts:login')

    check_like = tobacco.filter(like_user=profile)

    if check_like.exists():
        tobacco.like_user.remove(profile)
        tobacco.total_like -= 1
        tobacco.save()

    else:
        tobacco.like_user.add(profile)
        tobacco.total_like += 1
        tobacco.save()

    return redirect('cigarettes:detail', cigarette_id)

def comment(request, cigarette_id):

    if request.method == "POST":
        comment = Comment()
        comment.belongs_to_tobacco = Tobacco.objects.get(id=cigarette_id)
        try:
            user = request.user
            profile = Profile.objects.get(user=user)
            comment.belongs_to_user = profile
            comment.feel_of_hit = request.POST['feel_of_hit']
            comment.score = request.POST['score']
            comment.content = request.POST['content']
            comment.save()
        except: #유저 로그인 안했을 경우
            return redirect('accounts:login')
        return redirect('cigarettes:detail', cigarette_id)
    else:
        try:
            user = request.user
            profile = Profile.objects.get(user=user)
            context = {'profile': profile, 'cigarette_id':cigarette_id}
        except: #유저 로그인 안했을 경우
            return redirect('accounts:login')
        return render(request, 'cigarettes/comment.html', context)
    return redirect('tobacco:detail', cigarette_id)

def new_cigarette(request):
    mode = "create"
    tobacco_type = "cigarette"
    context = {'tobacco_type' : tobacco_type, 'mode' : mode}
    return render(request, 'cigarettes/create_tobacco.html', context)

def new_elec_cigarette(request):
    tobacco_type = "elec_cigarette"
    return render(request, 'cigarettes/create_tobacco.html', {'tobacco_type' : tobacco_type})

def create_cigarette(request):
    cigarette = Cigarettes()
    cigarette.is_local = request.POST.get('is_local')
    cigarette.brand = request.POST.get('brand')
    cigarette.name = request.POST.get('name')
    cigarette.photo = request.FILES.get('photo')
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

def edit_cigarette(request, edit_cigarette_id):
    mode = "update"
    tobacco_type = "cigarette"
    edit_cigarette = get_object_or_404(Tobacco, pk=edit_cigarette_id)
    context = {'tobacco_type' : tobacco_type, 'edit_cigarette' : edit_cigarette, 'mode' : mode}

    return render(request, 'cigarettes/create_tobacco.html', context)


# def update_cigarette(request, update_cigarette_id):
#     cigarette = Cigarettes()
#     cigarette.is_local = request.POST.get('is_local')
#     cigarette.brand = request.POST.get('brand')
#     cigarette.name = request.POST.get('name')
#     cigarette.price = request.POST.get('price')
#     cigarette.TAR = request.POST.get('tar')
#     cigarette.nicotine = request.POST.get('nicotine')
#     cigarette.rel_date = request.POST.get('rel_date')
#     cigarette.is_menthol = request.POST.get('is_menthol')
#     cigarette.save()

#     #return redirect('//' +str(new_post.id))
#     return redirect('cigarettes:index')