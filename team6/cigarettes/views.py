from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Tobacco, Comment
from accounts.models import Profile

# Create your views here.
def index(request):
    return render(request, 'cigarettes/index.html')

def detail(request, tobacco_id):
    tobacco = get_object_or_404(Tobacco, pk = tobacco_id)
    comment_list = Comment.objects.filter(belongs_to_tobacco=tobacco)

    foh_dict = {'상':0,'중':0,'하':0}
    score = 0

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

def like(request, tobacco_id):

    tobacco = Tobacco.objects.get(id=tobacco_id)
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

    return redirect('cigarettes:detail', tobacco_id)

def comment(request, tobacco_id):

    if request.method == "POST":
        comment = Comment()
        comment.belongs_to_tobacco = Tobacco.objects.get(id=tobacco_id)
        try:
            user = request.user
            profile = Profile.objects.get(user=user)
            comment.belongsto_user = profile
            comment.feel_of_hit = request.POST['feel_of_hit']
            comment.score = request.POST['score']
            comment.content = request.POST['content']
            comment.save()
        except: #유저 로그인 안했을 경우
            return redirect('accounts:login')
        return redirect('cigarettes:detail', tobacco_id)
    else:
        try:
            user = request.user
            profile = Profile.objects.get(user=user)
        except: #유저 로그인 안했을 경우
            return redirect('accounts:login')
        return render(request, 'cigarettes/comment.html')