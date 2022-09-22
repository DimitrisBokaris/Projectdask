# import pymprog modeler functions
import pymprog

def solver1(): 
    # begin modelling
    model = pymprog.model('dovetail')

    # variables
    X12 = model.var('X12', kind=bool)
    X13 = model.var('X13', kind=bool)
    X14 = model.var('X14', kind=bool)
    X23 = model.var('X23', kind=bool)
    X24 = model.var('X24', kind=bool)
    X25 = model.var('X25', kind=bool)
    X35 = model.var('X35', kind=bool)
    X36 = model.var('X36', kind=bool)
    X45 = model.var('X45', kind=bool)
    X47 = model.var('X47', kind=bool)
    X57 = model.var('X57', kind=bool)
    X67 = model.var('X67', kind=bool)

    # objective
    model.minimize(6*X12+2*X13+16*X14+7*X23+5*X24+4*X25+8*X36+3*X35+4*X45+3*X47+10*X57+X67, 'z')

    # constraints
    X12+X13+X14==1
    -X12+X23+X24+X25==0
    -X13-X23+X36+X35==0
    -X14-X24+X45+X47==0
    -X35-X45-X25+X57==0
    -X36+X67==0
    -X67-X47-X57==-1
    # solve the problem
    model.solve()


    # print the value of the variables at the optimum
    print("X12=",X12.primal)
    print("X13=",X13.primal)
    print("X14=",X14.primal)
    print("X23=",X23.primal)
    print("X24=",X24.primal)
    print("X25=",X25.primal)
    print("X35=",X35.primal)
    print("X36=",X36.primal)
    print("X45=",X45.primal)
    print("X47=",X47.primal)
    print("X57=",X57.primal)
    print("X67=",X67.primal)
    print(" Z=" ,model.vobj())
    
if __name__=='__main__':
    solver1()
