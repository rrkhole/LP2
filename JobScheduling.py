class Job:
    def __init__(self, name1, profit1, deadline1):
        self.name = name1
        self.profit = profit1
        self.deadline = deadline1


class JobSet:
    def __init__(self,arr1):
        self.arr=arr1
        self.n=len(arr1)
    def QuickSortD(self,l,m):
        if l<m:
            p=self.partition(l,m)
            #print(p)
            self.QuickSortD(l,p)
            self.QuickSortD(p+1,m)
    def partition(self,l,m):
        p=self.arr[l].profit
        j=l
        i=m
        while i>j:
            if(i==l or j==m):
                break
            while(self.arr[i].profit<p and i>l):
                i=i-1
            #print(i)
            while(self.arr[j].profit>=p and j<m):
                j=j+1
            #print(j)
            if(j<i):
                self.arr[i],self.arr[j]=self.arr[j],self.arr[i]
                #print(i,j)
        self.arr[l],self.arr[i]=self.arr[i],self.arr[l]
        return i
    def display(self):
        for i in range(self.n):
            print(self.arr[i].profit)
    def Schedule(self):
        t=0
        for i in range(self.n):
            if self.arr[i].deadline>t:
                t=self.arr[i].deadline
        result=[False]*t    #to store whether current
                        # position is occupied or not
        job=['-1']*t    #Stores the sequence of jobs executed
        executed=[False]*self.n #To check if a job can be executed
                                #or not
        profit=0
        for i in range(self.n):
            for j in range(min(t-1,self.arr[i].deadline-1),-1,-1):
                if result[j]==False:
                    result[j]=True
                    executed[i]=True
                    job[j]=self.arr[i].name
                    profit+=self.arr[i].profit
                    break
        print("The maximum profit is %3d"%(profit))
        print("The sequence of execution of jobs is as follows:")
        for i in range(t):
            if(job[i]!='-1'):
                print(job[i])
        for i in range(self.n):
            if(executed[i]==False):
                print(self.arr[i].name+" Can't be executed!")

arr=[]
n=int(input("Enter no. of processes:"))

for i in range(n):
    name=input("Enter name of job:")
    profit=int(input("Enter profit:"))
    deadline=int(input("Enter deadline:"))
    job=Job(name,profit,deadline)
    arr.append(job)

job_set = JobSet(arr)

job_set.QuickSortD(0,n-1)

job_set.Schedule()

