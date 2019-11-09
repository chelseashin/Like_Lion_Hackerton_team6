from django.shortcuts import render
from cigarettes.models import Tobacco

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