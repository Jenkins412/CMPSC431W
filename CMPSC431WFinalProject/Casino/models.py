
# Create your models here.
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    ssn = models.CharField(max_length=9, unique=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    play_history_id = models.IntegerField(null=True, blank=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class AccountHistory(models.Model):
    account_user = models.OneToOneField(User, on_delete=models.CASCADE)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    games_played = models.IntegerField()
    total_wagered = models.DecimalField(max_digits=10, decimal_places=2)

class PlayHistory(models.Model):
    play_id = models.AutoField(primary_key=True)
    play_user = models.ForeignKey(User, on_delete=models.CASCADE)
    play_table_id = models.IntegerField()
    session_profit = models.DecimalField(max_digits=10, decimal_places=2)

class SignInHistory(models.Model):
    login_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_logins = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class CasinoGame(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=255)
    rules = models.TextField()
    min_wager = models.DecimalField(max_digits=10, decimal_places=2)
    max_wager = models.DecimalField(max_digits=10, decimal_places=2)
    min_table_buyin = models.DecimalField(max_digits=10, decimal_places=2)
    max_table_buyin = models.DecimalField(max_digits=10, decimal_places=2)

class Gameplay(models.Model):
    table_id = models.AutoField(primary_key=True)
    casino_game = models.ForeignKey(CasinoGame, on_delete=models.CASCADE)
    game_user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_balance = models.DecimalField(max_digits=10, decimal_places=2)
    hand_wager = models.DecimalField(max_digits=10, decimal_places=2)
    hand_result = models.CharField(max_length=3)