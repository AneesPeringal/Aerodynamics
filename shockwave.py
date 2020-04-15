#total pressure ratio comparison between  normal shock wave 
#and a n oblique shock wave followed by a normal shock wave

#let us find the total pressure ratio for normal shock wave for different M
import math
gamma=1.4
R=287
c_p=gamma*R/(gamma-1)

def normal_shock(M):
    del_S = c_p*math.log((1+(2*gamma*(M**2 -1))/(gamma+1))*(2+(gamma - 1 )*M**2)/((gamma+1)*(M**2)))-R*math.log(1+(2*gamma*(M**2-1)/(gamma+1)))
    ratio_P = math.exp(-del_S/R)
    return(ratio_P)


def oblique_shock(M,beta):

    theta = math.atan((2*((M**2 * math.sin(beta)**2)-1))/(math.tan(beta)*M**2*(gamma+math.cos(2*beta))+2))
    M_n1 = M * math.sin(beta)
    M_n2 = math.sqrt(abs((1+((gamma-1)/2*M_n1**2))/(gamma*M_n1**2 -(gamma-1)/2)))
    M_2 = M_n2/math.sin(beta-theta)
    #M_3 = math.sqrt((1+(gamma-1)*M_2**2/2)/(gamma*M_2**2 -(gamma-1)/2))
    ratio_P1 = normal_shock(M_n1)
    ratio_p2 = normal_shock(M_2)
    ratio_P = ratio_P1*ratio_p2
    return ratio_P
i=1.05
while i<100:
    j=0.5
    while j<1.5:
        if normal_shock(i)<oblique_shock(i,j):
            print ("condition")
            j=j+0.05
            continue
            
        else:
            print("false")
            print("M=",i)
            print(("beta=",math.degrees(j)))
            print()
            break
    i=i+0.05
