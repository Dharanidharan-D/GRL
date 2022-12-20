class main:
    class dataset:
        distance=int(input())
        time=int(input())
        speed=int(input())
    
    class Userinput(dataset):
        user=input()
        user=user.split(",")
        data=[]
        for i in range(len(user)):
            data.append(input())
        
    class Measure(Userinput):
        data1=[]
        for i in data:
            data1.append(i[0]*i[1])
            
    class Showresult(Userinput):
        for i in range(len(data1)):
            print(user[i],data1[i])