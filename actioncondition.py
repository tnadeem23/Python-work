import numpy as np


noofacts = input('Enter the number of actions you want to input : ')
acts = []
conds = []
ind=[]
indnew=[]
for i in range(0,int(noofacts)):
    opt=input('Enter action no '+str(i+1)+' : ');
    acts.append(opt)
for k in range(0,len(acts)):
    ind.append([])
noofconds = input('Enter the number of conditions you want to input : ')
for i in range(0,int(noofconds)):
    p = input('Enter condition no '+str(i+1)+' : ')
    conds.append(p)
n=2**(len(conds))
cond = np.zeros(((len(conds)),n),dtype ='int32')
act = np.zeros(((len(acts)),n),dtype ='int32')
act=act.astype(str)
act[:,:]='-'
for i in range(len(conds)):
    for j in range(n-1,-1,-1):
        cond[i][j] = j/(2**i)%2
cond=cond[::-1]
for i in range(n):
    for j in range(3):
        if cond[j][i]==0:
            if i not in ind[0]:
                ind[0].append(i)
            else:
                pass
for i in range(len(ind[0]),n):
    if np.array_equal(cond[3:,i],[0,0,0]):
        if i not in ind[1]:
            ind[1].append(i)
    if np.array_equal(cond[3:,i],[1,1,1]):
        if i not in ind[3]:
            ind[3].append(i)
    if np.array_equal(cond[3:,i],[0,0,1]) or np.array_equal(cond[3:,i],[0,1,0]) or np.array_equal(cond[3:,i],[1,0,0]):
        if i not in ind[2]:
            ind[2].append(i)
    if np.array_equal(cond[3:,i],[0,1,1]) or np.array_equal(cond[3:,i],[1,0,1]) or np.array_equal(cond[3:,i],[1,1,0]):
        if i not in ind[4]:
            ind[4].append(i)
    else:
        pass
print("\nAction 1 = Not a triangle")
print("Action 2 = Scalene triangle")
print("Action 3 = Isosceles triangle")
print("Action 4 = Equilateral triangle")
print("Action 5 = Not a triangle")
print("\nCondition 1 = a<b+c")
print("Condition 2 = b<a+c")
print("Condition 3 = c<a+b")
print("Condition 4 = a=b")
print("Condition 5 = a=c")
print("Condition 6 = b=c\n")
print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t'+"Original form")
for i in range(len(acts)):
    for index in ind[i]:
        act[i][index]='x'
for i in range(len(conds)):
    print("Condition "+str(conds[i])+" : ",end='')
    for j in range(n):
        print(str(cond[i][j])+" ",end='')
    print()
for i in range(len(acts)):
    print("Action "+str(acts[i])+" : ",end='')
    for j in range(n):
        print(str(act[i][j])+" ",end='')
    print()
q=2
indexa=-1
while q<len(ind[0]):
    q=q*2
    k=0
    indexa=indexa+1
    x=(len(cond[0,:])-8)/2
    indnew.append([])
    for j in range(int(x)):
        for i in range(len(conds)):
            if cond[i][k]!=cond[i][k+1]:
                cond[i][k]=8
        indnew[indexa].append(k+1)
        if j==0 and indexa==4:
            break
        k=k+2
    cond=np.delete(cond,indnew[indexa],1)
    act=np.delete(act,indnew[indexa],1)
    print("\t\t\t\tReduction no "+str(indexa+1)+" : ")
    for i in range(len(conds)):
        print("Condition "+str(conds[i])+" : ",end='')
        for j in range(len(cond[0,:])):
            print(str(cond[i][j])+" ",end='')
        print()
    for i in range(len(acts)):
        print("Action "+str(acts[i])+" : ",end='')
        for j in range(len(act[0,:])):
            print(str(act[i][j])+" ",end='')
        print()
