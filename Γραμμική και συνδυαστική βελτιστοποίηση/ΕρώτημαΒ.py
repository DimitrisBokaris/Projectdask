import numpy as np, matplotlib.pyplot as plt
plt.figure(figsize=(9,6.8))
plt.axis([0,10,0,10])
plt.ylabel('x\N{SUBSCRIPT TWO}')
plt.xlabel('''x\N{SUBSCRIPT ONE}\nΚόκκινο χρώμα για τις ευθείες με συντελεστή 1/2$\leq$c2$\leq$2, μαύρο για c2$\geq$2, κίτρινο για c2$\leq$1/2.Από τη γραμμοσκιασμένη\nπεριοχή, είναι φανερό ότι μόνο για τις κόκκινες ευθείες μπορεί να ελαχιστοποιείται η συνάρτηση Ζ στο σημείο (4/3,4/3).''')
plt.title("Ερώτημα (β)\n1/2$\leq$c2$\leq$2")
x1=np.linspace(0,10,100)
p1=4-2*x1
p2=2-1/2*x1
p3=6-6/5*x1
p4=36/7-6/7*x1
plt.plot(x1,p1,label='(Π1): 6x\N{SUBSCRIPT ONE}+3x\N{SUBSCRIPT TWO}=12')
plt.plot(x1,p2,label='(Π2): 4x\N{SUBSCRIPT ONE}+8x\N{SUBSCRIPT TWO}=16')
plt.plot(x1,p3,label='(Π3): 6x\N{SUBSCRIPT ONE}+5x\N{SUBSCRIPT TWO}=30')
plt.plot(x1,p4,label='(Π4): 6x\N{SUBSCRIPT ONE}+7x\N{SUBSCRIPT TWO}=36')
floatlist1=[0.6,1,1.4,1.8]
floatlist2=[0.1,0.2,0.3,0.4]
for i in range(3,8):
    f=1/i*(4/3-x1)+4/3
    plt.plot(x1,f,'k:')
for i in floatlist2:
    f=1/i*(4/3-x1)+4/3
    plt.plot(x1,f,'y:')
for i in floatlist1:
    f=1/i*(4/3-x1)+4/3
    plt.plot(x1,f,'r:')
m1=np.maximum(p1,p2)
m2=np.minimum(p3,p4)
plt.fill_between(x1, m1, m2, color='grey', alpha=0.5)
plt.legend()
a=np.array([[6,3],[4,8]])
b=np.array([12,16])
x=np.linalg.solve(a,b)
plt.annotate("Σημείο τομής των ευθειών\n6x\N{SUBSCRIPT ONE}+3x\N{SUBSCRIPT TWO}=12 ,4x\N{SUBSCRIPT ONE}+8x\N{SUBSCRIPT TWO}=16\nx\N{SUBSCRIPT ONE}=4/3,x\N{SUBSCRIPT TWO}=4/3,Ζ=4/3(1+c2)",xy=(4/3,4/3),xytext=(3,4.5),arrowprops=dict(facecolor='black', width=1, shrink=0.05))
plt.plot(x[0],x[1],"o:k")
plt.show()
