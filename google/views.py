from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    # ユーザ名取得
    print(f"Current user: {request.user.username}")
    # 全ユーザ情報取得
    for attr in dir(request.user):
        try:
            print(f"{attr}: {getattr(request.user, attr)}")
        except AttributeError:
            print(f"{attr}: [アクセス不可]")
    # HTML
    return render(request, 'home.html')
