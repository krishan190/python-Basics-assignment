from datetime import datetime
dt = datetime.today();
print(dt)                                 # 2022-09-26 04:29:54.393414

d1 = dt.strftime("%d-%m-%Y and  %I:%M:%p")  
print(d1)                                 #26-09-2022 and  04:29;AM

d1 = dt.strftime("%d/%b/%Y")
print(d1)                                  #26/Sep/2022

d1 = dt.strftime("%d-%m-%y")
print(d1)                                # 26-09-22

d1 = dt.strftime("%H : %M : %S")
print(d1)                                 #04 : 29 : 54

d1 = dt.strftime("%B %d %Y")
print(d1)                                 #September 26 2022

d1 = dt.strftime("%d / %b / %Y")
print(d1)                                 #26 / Sep / 2022