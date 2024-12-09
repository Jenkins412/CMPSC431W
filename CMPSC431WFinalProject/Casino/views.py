# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def create_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        ssn = request.POST['ssn']
        fname = request.POST['fname']
        lname = request.POST['lname']
        if not username or not password or not ssn or not fname or not lname:
            return JsonResponse({'error': 'All fields are required.'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already taken.'}, status=400)
        if User.objects.filter(ssn=ssn).exists():
            return JsonResponse({'error': 'Social security number already linked to account.'}, status=400)
        user = User.objects.create(username=username, password=password, ssn=ssn, fname=fname, lname=lname, account_balance = 0)
        user.save()
        return render(request, "join_table.html")
    return render(request, 'create_account.html')    

from django.contrib.auth.hashers import check_password

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return JsonResponse({'message': 'Sign in successful', 'user_id': user.id})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=404)
        
def deposit_money(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        deposit_amount = float(request.POST['deposit_amount'])
        
        user = User.objects.get(id=user_id)
        user.account_balance += deposit_amount
        user.save()
        return JsonResponse({'message': 'Deposit successful', 'new_balance': user.account_balance})
    
from .models import Gameplay, PlayHistory

def join_table(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        table_buyin = float(request.POST['table_buyin'])
        table_number = int(request.POST['table_number'])
        
        user = User.objects.get(id=user_id)
        if user.account_balance >= table_buyin:
            user.account_balance -= table_buyin
            user.save()

            play_history = PlayHistory.objects.create(play_user=user, play_table_id=table_number)
            Gameplay.objects.create(table_id=table_number, game_user=user, table_balance=table_buyin)
            
            return JsonResponse({'message': 'Joined table successfully', 'new_balance': user.account_balance})
        else:
            return JsonResponse({'message': 'Insufficient balance'}, status=400)

def place_bet(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        table_number = int(request.POST['table_number'])
        bet = float(request.POST['bet'])
        
        user = User.objects.get(id=user_id)
        if user.account_balance >= bet:
            user.account_balance -= bet
            user.save()
            
            gameplay = Gameplay.objects.get(table_id=table_number, game_user=user)
            gameplay.hand_wager = bet
            gameplay.save()
            
            return JsonResponse({'message': 'Bet placed successfully', 'new_balance': user.account_balance})
        else:
            return JsonResponse({'message': 'Insufficient balance'}, status=400)


