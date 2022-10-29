print("T4")
M = float(input("The number of kilometers to the destination :"))
print("The trip just went 1")
print("A trip to go and return 2")
if M < 60 :
 RB = float(input(""))
 if RB == 1:
    V = M
    ASD=V*1500
    print(ASD)
 elif RB == 2:
    MM=(M*2)
    AASSDD=(MM-60)*3000
    print(AASSDD)
elif M > 60 or M ==60:
 RB = float(input(""))
 if RB == 1:
    V=(M+0)
    ASD1=(V * 1500)
    ASD=(V - 60)*3000
    print(ASD + ASD1)
 elif RB == 2:
     V = (M + 0)
     ASD1 = (V * 1500)
     ASD = (V - 60) * 3000
     print((ASD + ASD1) * 2)
