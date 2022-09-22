import numpy as np, matplotlib.pyplot as plt
plt.figure(figsize=(9,6.8))
plt.axis([0,10,0,10])
plt.ylabel('x\N{SUBSCRIPT TWO}')
plt.xlabel('x\N{SUBSCRIPT ONE}\nΑπό το σχήμα φαίνεται ότι οι ευθείες που μπορούν να έχουν μέγιστο στο σημείο (2.5,3), είναι αυτές\nόπου -6/5$\leq$c1/c2$\leq$-6/7, δηλαδή οι κόκκινες. (Ανάμεσα στους συντελεστές του περιορισμού Π3 και Π4).')
plt.title("Ερώτημα (γ)\n-6/5$\leq$c1/c2$\leq$-6/7")
x1=np.linspace(0,10,100)
p1=4-2*x1
p2=2-1/2*x1
p3=6-6/5*x1
p4=36/7-6/7*x1
plt.plot(x1,p1,label='(Π1): 6x\N{SUBSCRIPT ONE}+3x\N{SUBSCRIPT TWO}=12')
plt.plot(x1,p2,label='(Π2): 4x\N{SUBSCRIPT ONE}+8x\N{SUBSCRIPT TWO}=16')
plt.plot(x1,p3,label='(Π3): 6x\N{SUBSCRIPT ONE}+5x\N{SUBSCRIPT TWO}=30')
plt.plot(x1,p4,label='(Π4): 6x\N{SUBSCRIPT ONE}+7x\N{SUBSCRIPT TWO}=36')
for i in range(2,4):
    p4n=3+i*(2.5-x1)
    plt.plot(x1,p4n,'k:')
floatlist1=[0.1,0.3,0.5,0.7]
for i in floatlist1:
    p4n=3+i*(2.5-x1)
    plt.plot(x1,p4n,'y:')
floatlist2=[0.87,0.95,1.03,1.12]
for i in floatlist2:
    p4n=3+i*(2.5-x1)
    plt.plot(x1,p4n,'r:')
m1=np.maximum(p1,p2)
m2=np.minimum(p3,p4)
plt.fill_between(x1, m1, m2, color='grey', alpha=0.5)
plt.legend()
a=np.array([[6,5],[6,7]])
b=np.array([30,36])
x=np.linalg.solve(a,b)
Z=3*x[0]+x[1]
plt.annotate("\nΣημείο τομής των ευθειών\n6x\N{SUBSCRIPT ONE}+5x\N{SUBSCRIPT TWO}=30 ,6x\N{SUBSCRIPT ONE}+7x\N{SUBSCRIPT TWO}=36  \nx\N{SUBSCRIPT ONE}={}, x\N{SUBSCRIPT TWO}={}, max(Z)={}".format(x[0],x[1],Z),xy=(x[0],x[1]),xytext=(3.2,5.3),arrowprops=dict(facecolor='black', width=1, shrink=0.05))
plt.plot(x[0],x[1],"o:k")
plt.show()
