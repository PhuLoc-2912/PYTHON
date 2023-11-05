'''
usd = int(input("Nhập số USD: "))
vnd = usd * 24592
print(str(usd), " USD =", str(vnd),"VNĐ")
'''
#
'''
import random

def play_game(player_choice):
    choices = ["kéo", "búa", "bao"]
    computer_choice = random.choice(choices)

    print(f"Người chơi: {player_choice}")
    print(f"Máy tính: {computer_choice}")

    if player_choice == computer_choice:
        print("Hòa!")
    elif (
        (player_choice == "kéo" and computer_choice == "bao") or
        (player_choice == "búa" and computer_choice == "kéo") or
        (player_choice == "bao" and computer_choice == "búa")
    ):
        print("Người chơi thắng!")
    else:
        print("Máy tính thắng!")

# Chương trình chính
print("Chào mừng bạn đến với trò chơi kéo búa bao!")
print("Bạn có thể chọn kéo, búa hoặc bao.")

valid_choices = ["kéo", "búa", "bao"]
while True:
    player_choice = input("Lựa chọn của bạn: ").lower()
    if player_choice in valid_choices:
        play_game(player_choice)
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
'''
#
'''
from random import randint

while True:
    nguoichoi = input("Chọn kéo, búa hoặc bao: ")
    maytinh = randint(0, 2)

    if maytinh == 0:
        maytinh = "kéo"
    elif maytinh == 1:
        maytinh = "búa"
    else:
        maytinh = "bao"

    print("-------------------------")
    print("Người chơi chọn:", nguoichoi)
    print("Máy tính chọn:", maytinh)
    print("-------------------------")

    if nguoichoi == maytinh:
        print("Người chơi hoà.")
    elif nguoichoi == "kéo":
        if maytinh == "búa":
            print("Người chơi thua.")
        else:
            print("Người chơi thắng.")
        break
    elif nguoichoi == "búa":
        if maytinh == "kéo":
            print("Người chơi thắng.")
        else:
            print("Người chơi thua.")
        break
    elif nguoichoi == "bao":
        if maytinh == "kéo":
            print("Người chơi thua.")
        else:
            print("Người chơi thắng.")
        break
    else:
        print("Vui lòng nhập lại, chọn kéo, búa hoặc bao.")
'''
count = 0
while count < 5:
    print(count)
    count += 1  

