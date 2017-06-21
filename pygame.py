# -*- coding: utf-8 -*-
import random

ST=[]
t=0
while t<4 :
    tem=str(random.randrange(0,9))
    if not (tem in ST):
        ST.append(tem)
        t+=1
#宣告一個ST
#存放亂數產生要猜的一組不重覆的四位數{
time=1

while True:
    print ("猜第%d次。\n請輸入一個不重覆的四位數字或輸入'STOP'以退出遊戲:" %time)
    A=0
    B=0
	
    input_s=input()
    if "STOP" in input_s.upper():
        print ("離開遊戲! 正確答案為 %s" % "".join(str(n) for n in ST))
        break
		
    else:
        try:
            int(input_s)    
			#測試是否輸入的為數字,若非會產生列外處理
            if "".join(str(n) for n in ST)==input_s: 
			#猜到數字,結束遊戲
                print ("Good Job!! 共猜了 %d 次") %time
                break
            elif len(input_s) != 4:
                print ("錯誤! 不正確的長度!\n")
            else:   
			#未猜到,計算與目標數字的差異
                for tem in range(4):
                    if ST[tem] == input_s[tem]: 
					#包括、且位置相符
                        A+=1
                    if input_s[tem] in ST:  
					#計算包括的數字,所以需再減去A的總合,才是僅包括,但位置不同的數量
                        B+=1
                print ("%d A\t%d B"% (A,B-A))
                time+=1
        except:
            print ("錯誤! 內含非數字的字串\n")
system("pause")
