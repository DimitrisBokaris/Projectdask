import numpy as np, matplotlib.pyplot as plt
plt.axis([0,10,0,10])
plt.ylabel('x\N{SUBSCRIPT TWO}')
plt.xlabel('x\N{SUBSCRIPT ONE}')
plt.title("Ερώτημα (α)")
x1=np.linspace(0,10,100)
p1=4-2*x1
p2=2-1/2*x1
p3=6-6/5*x1
p4=36/7-6/7*x1
plt.plot(x1,p1,label='(Π1): 6x\N{SUBSCRIPT ONE}+3x\N{SUBSCRIPT TWO}=12')
plt.plot(x1,p2,label='(Π2): 4x\N{SUBSCRIPT ONE}+8x\N{SUBSCRIPT TWO}=16')
plt.plot(x1,p3,label='(Π3): 6x\N{SUBSCRIPT ONE}+5x\N{SUBSCRIPT TWO}=30')
plt.plot(x1,p4,label='(Π4): 6x\N{SUBSCRIPT ONE}+7x\N{SUBSCRIPT TWO}=36')
for i in range(6,17,3):
    f=i-3*x1
    plt.plot(x1,f,'k:',label='3x\N{SUBSCRIPT ONE}+x\N{SUBSCRIPT TWO}={}'.format(i))
m1=np.maximum(p1,p2)
m2=np.minimum(p3,p4)
plt.fill_between(x1, m1, m2, color='grey', alpha=0.5)
plt.legend()
a=np.array([[6,5],[0,1]])
b=np.array([30,0])
x=np.linalg.solve(a,b)
Z=3*x[0]+x[1]
plt.annotate("\nH λύση είναι το σημείο τομής\nτων ευθειών 6x\N{SUBSCRIPT ONE}+5x\N{SUBSCRIPT TWO}=30 ,x\N{SUBSCRIPT TWO}=0  \nΆρα x\N{SUBSCRIPT ONE}={}, x\N{SUBSCRIPT TWO}={}, max(Z)={}".format(x[0],x[1],Z),xy=(x[0],x[1]),xytext=(4.5,2.5),arrowprops=dict(facecolor='black', width=1, shrink=0.05))
plt.plot(x[0],x[1],"o:k")
plt.show()
