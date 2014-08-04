import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from snake.models import Score

@login_required
def snake(request):
    return render(request, 'snake.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()

    return render(request, 'registration/register.html',{
        'form': form
    })



def home(request):
    return render(request, 'base.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@csrf_exempt
def save_score(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        game = data['game']
        score = data['score']
        player = request.user

        new_score = Score.objects.create(
            player=player,
            score=score,
            game=game
        )

        score_info = {
            'player': new_score.player.username,
            'score': new_score.score,
            'game': new_score.game
        }

        return HttpResponse(json.dumps(score_info), content_type='application/json')

@csrf_exempt
def get_score(request):
    scores = Score.objects.filter(player=request.user)
    highscore = scores.aggregate(Max('score'))


    data = {'highscore': highscore}

    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def leaderboard(request):
    if request.method == "GET":
        scores = Score.objects.order_by('-score')
        data = {'scores': scores}

    return render(request, 'leaderboard.html', data)


# @csrf_exempt
# def get_leaders(request):
#     scores = Score.objects.order_by('-score')
#     data = {'scores': scores}
#
#     return render(request, 'leaderboard.html')


