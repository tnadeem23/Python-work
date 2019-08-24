import pandas as pd
import numpy as np
population = np.zeros((10,2))
randnums = np.random.randint(-5,5, size=(10,2))
population = randnums
bsflist=np.zeros((40,10),dtype='float32')
avgfitnesslist=np.zeros((40,10),dtype='float32')
for x in range(10):
    for y in range(40):
        print('Population: ')
        print(population)
        def fitness(poporoff):
            fitnessalgo = []
            for i in range(10):
                fitnessvalues = ((poporoff[i,0])**2)+((poporoff[i,1])**2)
                fitnessalgo.append(fitnessvalues)
            fitnessalgo = np.asarray(fitnessalgo)
            return fitnessalgo
        fitnesspop = fitness(population)
        print("Fitness of Population: ")
        print(fitnesspop)
        finalselection = []
        for i in range(5): #crossover
            A = np.random.randint(10)
            B = np.random.randint(10)
            selectionA = population[A]
            selectionB = population[B]
            finalselection.append(selectionA)
            finalselection.append(selectionB)
        finalselection = np.asarray(finalselection)
        print('Selected Elements for Crossover: ')
        print(finalselection)
        for i in range(0,9,2):
            temp = finalselection[i,1]
            finalselection[i,1] = finalselection[i+1,1]
            finalselection[i+1,1] = temp
        offspring = finalselection
        print('Selected Elements after Crossover:  ')
        print(offspring)
        offspring = offspring.astype('float32')
        for i in range(10):#mutation
            randmutation = np.random.randint(0,2)
            #print(randmutation)
            if i >= 5 :
                offspring[i,randmutation] = offspring[i,randmutation]-0.25
            else :
                offspring[i,randmutation] = offspring[i,randmutation]+0.25
        print('Offsprings: ')
        print(offspring)
        fitnessoff = fitness(offspring)
        print('Offsprings Fitness: ')
        print(fitnessoff)
        #fitnesspop = fitnesspop.astype('float32')
        totalfitness = np.concatenate([fitnesspop,fitnessoff])
        print('Population and Offsprings:')
        #totalfitness = np.concatenate([population,offspring])
        print('Total Fitness: ')
        print(totalfitness)
        fitnesssum = np.sum(totalfitness)
        print('Fitness Sum: ')
        print(fitnesssum)
        probability = []
        for i in range(20):
            prob = totalfitness[i]/fitnesssum
            probability.append(prob)
        print('Fitness Probabilites: ')
        print(probability)
        print('Fitness Probabilites Sum: ')
        print(np.sum(probability))
        commrange = []
        rang = 0
        for i in range(20):
            rang = rang + probability[i]
            commrange.append(rang)
        print(commrange)
        index=[]
        commrange = np.asarray(commrange)
        #commrange.astype('float64')
        for i in range(10):
            randnumrange = np.random.uniform(0,1)
            print('Random Num range :' ,randnumrange)
            for j in range(20):
                if randnumrange<commrange[0]:
                    index.append(0)
                    break
                elif randnumrange>=commrange[j-1] and randnumrange<commrange[j]:
                    index.append(j)
                    break
                else:
                    pass
        print('Indexes of the selected ones: ')
        print(index)
        finalones=[]
        finalonesfitness=[]
        population = population.astype('float64')
        offspring = offspring.astype('float64')
        popandoff = np.concatenate([population,offspring])
        print('Population and Offspring: ')
        print(popandoff)
        #print(finalones)
        #print(population)
        #print(offspring)

        for i in index:
            for j in range(10):
                final=popandoff[i]
                finalones.append(final)
                break
        finalones = np.asarray(finalones)
        print("Final Ones: ")
        print(finalones)
        for i in index:
            for j in range(10):
                final=totalfitness[i]
                finalonesfitness.append(final)
                break
        finalones = np.asarray(finalones)
        finalonesfitness = np.asarray(finalonesfitness)
        print("Final Ones: ")
        print(finalones)
        print("Final Ones Fitness: ")
        print(finalonesfitness)
        print("Average Fitness: ")
        avg = np.sum(finalonesfitness)/len(finalonesfitness)
        print(avg)
        bsfvalue = np.amax(finalonesfitness)
        bsflist[y,x]=bsfvalue
        avgfitnesslist[y,x] = avg
        print('Best survived fitness: ', bsfvalue)
        print('BSF: ',bsflist)
        population = finalones


cols_bsf = []
cols_bsf2= []
cols_avgfit  = []
cols_avgfit2  = []
avg_bsf = np.mean(bsflist,axis=1)
avg_fit = np.mean(avgfitnesslist,axis=1)
for i in range(10):
    cols_bsf.append('Run #' + str(i+1) + ' BSF')
    cols_avgfit.append('Run #' + str(i+1) + ' Avg Fit')
df_bsf = pd.DataFrame(bsflist,columns=cols_bsf)
cols_bsf2.append('Average BSF')
df_bsf2 = pd.DataFrame(avg_bsf,columns=cols_bsf2)
bsforg = pd.concat([df_bsf, df_bsf2], axis=1)
df_avg = pd.DataFrame(avgfitnesslist,columns=cols_avgfit)
cols_avgfit2.append('Average Fitness')
df_avg2 = pd.DataFrame(avg_fit,columns=cols_avgfit2)
avgfitorg = pd.concat([df_avg, df_avg2], axis=1)
print(bsforg)
print(avgfitorg)

df_bsf.to_csv('AverageBSF.csv',index=False)
df_avg.to_csv('AverageFitness.csv',index=False)

import matplotlib
import matplotlib.pyplot as plt
t = [i+1 for i in range(40)]
fig, ax = plt.subplots()
ax.plot(t,df_bsf2)
ax.set(xlabel='Generations', ylabel='Average BSF',
       title='Generations compared to Average BSF',)
ax.grid()

fig.savefig("test1.png")
plt.show()

t = [i+1 for i in range(40)]
fig, ax = plt.subplots()
ax.plot(t,df_avg2)
ax.set(xlabel='Generations', ylabel='Average Fitness',
       title='Generations compared to Average Fitness')
ax.grid()

fig.savefig("test2.png")
plt.show()

dffinal=pd.DataFrame({'Generations': range(1,41), 'Average Fitness': df_avg2['Average Fitness'], 'Average BSF': df_bsf2['Average BSF']})
plt.plot( 'Generations', 'Average Fitness', data=dffinal, marker='', color='red', linewidth=2)
plt.plot( 'Generations', 'Average BSF', data=dffinal, marker='', color='black', linewidth=2, linestyle='dashed', label="Average BSF")
plt.grid()
#fig.savefig("test3.png")
plt.legend()
plt.show()