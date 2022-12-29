class Main:
    
    def dataset(self):
        print('dataset')
        self.distance=int(input())
        self.time=int(input())
        self.speed=int(input())

    def Userinput(self):
        print('userinput')
        self.user=input()
        self.user=self.user.split(",")
        self.data=[]
        for i in range(len(self.user)):
            x=int(input())
            y=int(input())
            self.data.append([x,y])

    def Measure(self):
        self.data1=[]
        for i in self.data:
            self.data1.append(i[0]*i[1])

    def Showresult(self):
        for i in range(len(self.data1)):
            print(self.user[i],self.data1[i])
            
dharani=Main()
dharani.dataset()
dharani.Userinput()
dharani.Measure()
dharani.Showresult()
