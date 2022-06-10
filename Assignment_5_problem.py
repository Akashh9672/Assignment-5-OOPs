class power:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
        
    def nthpower(self,ans=0):
        self.ans=ans
        self.ans=self.n1**self.n2
        print("n'th power of given number:",self.ans)
n1=int(input("Enter any number:"))
n2=int(input("Enter the n power required:"))

power_obj=power(n1,n2)
power_obj.nthpower()
