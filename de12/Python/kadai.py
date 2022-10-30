from random import random
from re import I
from tkinter import Y

counter=0

print("99を超えないように限界まで挑戦してください。")
print("現在の数字は0です。")
while counter<=39:
    a =random.randint(1,7)
    
    quesution=input("まだ足しますか。")
    if quesution=="yes":
        counter=counter+a
        print("現在の合計は",counter,"です。")
    elif quesution=="no":
        print("ハイスコアは",counter,"です。")
        break
    elif counter==39:
        print("おめでとうございます。39ぴったりです。")
        break

else:
    print("39をこえました。失敗です。")

