#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np
import matplotlib.pyplot as plt
import sys
import io
from contextlib import redirect_stdout


# ###  INPUT PARAMETERS

# In[2]:


a=100 #we have 100 units of substance 'a' in the solution
b=100
c=100

t_max=500 #this is the time after which the reactivity of the compounds in this solution will be exhausted

pab=0.4 #this is the probability with which 'ab' compounds will form
pac=0.2 
pbc=0.4

tox_limit=0.1 #this is the toxicity limit. if it is exceeded, the solution with the formed compounds will become toxic


# ### SIMULATION

# In[3]:


def draw(a,b,c,t_max,pab,pac,pbc):
    i=1 #first iteration
    A=[a] #this array stores values indicating the amount of substance “a” in a given iteration
    B=[b]
    C=[c]
    AB=[0] #this array stores values indicating the amount of “ab” compounds in a given iteration
    AC=[0] #this is the toxic compound!!!!!!
    BC=[0]
    t=[0] #time units (iterations)
    
    tox_result=0 #indicates the number of cases where the simulation ended because the toxicity limit was reached (needed later)
    over_time=0 #indicates the number of cases where the simulation ended because of reaching t_max

    while i<=t_max:
        draw_1=random.randint(1,3) #we draw two substances: 1 means A, 2 means B, and 3 means C
        draw_2=random.randint(1,3)
        if draw_1+draw_2==2: #2xa - nothing changes
            A.append(a)
            B.append(b)
            C.append(c)
            AB.append(0)
            AC.append(0)
            BC.append(0)
        elif draw_1==draw_2 and draw_1+draw_2==4: #2xb - nothing changes
            A.append(a)
            B.append(b)
            C.append(c)
            AB.append(0)
            AC.append(0)
            BC.append(0)   
        elif draw_1+draw_2==6: #2xb - nothing changes
            A.append(a)
            B.append(b)
            C.append(c)
            AB.append(0)
            AC.append(0)
            BC.append(0) 
        elif draw_1+draw_2==3: #we drew A and B (the order does not matter)
            draw_ab=np.random.rand() #we draw a number between 0-1. if is <= the probability, the compound will be formed
            if draw_ab <= pab:
                a=a-1 #changing the amount of available substrates
                b=b-1
                A.append(a)
                B.append(b)
                C.append(c)
                AB.append(1) #changing the amount of the compound
                AC.append(0)
                BC.append(0)  
            else: 
                A.append(a)  #the case where nothing changes (because of the probability of compound forming)
                B.append(b)
                C.append(c)
                AB.append(0)
                AC.append(0)
                BC.append(0) 
        elif draw_1!=draw_2 and draw_1+draw_2==4: #we drew A and C (the order does not matter)
            draw_ac=np.random.rand() #we draw a number between 0-1. if is <= the probability, the compound will be formed
            if draw_ac <= pac:
                a=a-1 #changing the amount of available substrates
                c=c-1
                A.append(a)
                B.append(b)
                C.append(c)
                AB.append(0)
                AC.append(1) #changing the amount of the compound
                BC.append(0)   
            else:
                A.append(a) #the case where nothing changes (because of the probability of compound forming)
                B.append(b)
                C.append(c)
                AB.append(0)
                AC.append(0)
                BC.append(0) 
        elif draw_1+draw_2==5: #we drew B and C (the order does not matter)
            draw_bc=np.random.rand() #we draw a number between 0-1. if is <= the probability, the compound will be formed
            if draw_bc <= pbc:
                b=b-1 #changing the amount of available substrates
                c=c-1
                A.append(a)
                B.append(b)
                C.append(c)
                AB.append(0)
                AC.append(0)
                BC.append(1) #changing the amount of the compound  
            else:
                A.append(a) #the case where nothing changes (because of the probability of compound forming)
                B.append(b)
                C.append(c)
                AB.append(0)
                AC.append(0)
                BC.append(0) 

        sum_all=0
        sum_all=A[i]+B[i]+C[i]+sum(AB)+sum(AC)+sum(BC) #summarizes the number of objects in a given iteration
        
        t.append(i)
        
        if sum(AC) >= sum_all*tox_limit: #checking if the number of AC objects is greater than the sum of all*the given boundary
            print(f"!!!!The TOXICITY LIMIT has been reached!!!! (in iteration number {i})")
            tox_result+=1
            break
            
        if a<=0 or b<=0 or c<=0: # checking whether the substrates have run out
            print(f"!!!!The substrates has been exhausted!!!! (in iteration number {i})")
            break
        if i==t_max: 
            print(f"!!!!The time in which the reaction can take place is over!!!!")
            over_time+=1
            break
        i+=1

    return(A,B,C,AB,AC,BC,t,tox_result,over_time)


# ### RESULT

# In[4]:


A,B,C,AB,AC,BC,t,tox_result,over_time=draw(a,b,c,t_max,pab,pac,pbc) #calling the function


# ### PLOTTING

# In[5]:


#PLOTTING

plt.plot(A,'-',label="substrate A",color='black')
plt.plot(B,'-',label="substrate B",color='gray')
plt.plot(C,'-',label="substrate C",color='red')
plt.annotate(f'{A[-1]}', (len(A)-1, A[-1]), textcoords="offset points", xytext=(0,10), ha='center', color='black')
plt.annotate(f'{B[-1]}', (len(B)-1, B[-1]), textcoords="offset points", xytext=(0,10), ha='center', color='gray')
plt.annotate(f'{C[-1]}', (len(C)-1, C[-1]), textcoords="offset points", xytext=(0,10), ha='center', color='red')
plt.ylabel("number of substrates")
plt.xlabel("iterations")
plt.title("Change in the number of substrates in successive iterations") 
plt.legend()
plt.grid(True)
plt.show()

i=1
while i< len(AB):
    AB[i]=(AB[i-1]+AB[i]) #adds the number of objects in each iteration (earlier there was zeros and ones)
    i=i+1
i=1
while i< len(AC):
    AC[i]=(AC[i-1]+AC[i])
    i=i+1
i=1
while i< len(BC):
    BC[i]=(BC[i-1]+BC[i])
    i=i+1
    
plt.plot(t,AB,'-',label="compound AB",color='black')
plt.plot(t,AC,'-',label="compound AC",color='red')
plt.plot(t,BC,'-',label="compound BC",color='gray')
plt.legend()
plt.grid(True)
plt.xlabel("iterations")
plt.ylabel("number of compounds")
plt.title("The number of compounds formed in successive iterations")
plt.annotate(f'{AB[-1]}', (t[-1], AB[-1]), textcoords="offset points", xytext=(0,10), ha='center', color='black')
plt.annotate(f'{AC[-1]}', (t[-1], AC[-1]), textcoords="offset points", xytext=(0,10), ha='center', color='red')
plt.annotate(f'{BC[-1]}', (t[-1], BC[-1]), textcoords="offset points", xytext=(0,10), ha='center', color='gray')
plt.show()


# ### STATS

# In[6]:


i=0
simulations=1000 #running the model many times (1000 by default) to see what the outcome will be with given parameters

iterations=[]
tl=0 #value holder for the number of simulations ended because the toxicity limit was reached
tm=0 #value holder for the number of simulations ended because t_max was reached

while i<simulations:
    with io.StringIO() as buf, redirect_stdout(buf): #calling the "draw" function ignoring the prints inside it
        A,B,C,AB,AC,BC,t,tox_result,over_time=draw(a,b,c,t_max,pab,pac,pbc)  
    iterations.append(max(t))
    tl+=tox_result #adding up all the times the simulation ended because the toxicity limit was reached
    tm+=over_time
    i+=1

print(f"{(tl/simulations)*100}% of simulations endend because the toxicity limit was reached. For different outcome, please choose different input parameters.")
print(f"{(tm/simulations)*100}% of simulations endend because t_max was reached. For different outcome, please choose different input parameters.")


# In[ ]:





# In[ ]:




