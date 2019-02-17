a =[1,12,4,5]
ab = (x for x in a)

def fun1(ab):
    print(ab.__next__())
    fun1(ab)
print(a==True)
if a:
    print(23)
    a=[]
    if a:
        print(33)

