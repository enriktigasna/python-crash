import hashlib
import msvcrt
import random
import hmac
import sys
import time

# Constants
balance = 100
TIMEOUT = 1
e = 2**52
salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"

def get_hash():
    return str(random.getrandbits(128))

def get_result():
    hash_value = get_hash()

    hm = hmac.new(str.encode(hash_value), b'', hashlib.sha256)
    hm.update(salt.encode("utf-8"))
    h = hm.hexdigest()
    if int(h, 16) % 33 == 0:
        return 1
    h = int(h[:13], 16)
    e = 2**52
    return (((100 * e - h) / (e-h)) // 1) / 100.0

# Gives the user one second to send an input; otherwise, it returns the default value
def read_input(caption, default):
    start_time = time.time()
    sys.stdout.write(caption)
    sys.stdout.flush()
    user_input = ''
    
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getche()
            if ord(byte_arr) == 13:  # Enter key
                break
            elif ord(byte_arr) >= 32:  # Space character
                user_input += "".join(map(chr, byte_arr))
        if len(user_input) == 0 and (time.time() - start_time) > TIMEOUT:
            break
    
    print('')  # Needed to move to the next line
    return user_input if len(user_input) > 0 else default

def play_round(bet):
    crash = get_result()

    multiplier = 0
    while read_input(f"Current multiplier: {multiplier}. Current return: {bet * multiplier}", "NaN") == "NaN":
        print("PRESS SPACE THEN ENTER TO CASH OUT")
        multiplier += 0.1
        multiplier = round(multiplier, 1)

        if multiplier >= crash:
            multiplier = 0
            print("You crashed! ")
            break
    bet_return = round(multiplier * bet, 1)
    print(f"You made {bet_return}")
    return bet_return

while True:
    to_bet = input(f"How much do you want to bet? Your current balance is {balance}. ")
    try:
        to_bet = int(to_bet)
    except ValueError:
        print("Not a number!")
        continue

    if to_bet > balance:
        print("Insufficient Funds. Try again.")
        continue
    balance -= to_bet
    balance += play_round(to_bet)
