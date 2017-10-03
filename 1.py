#!/usr/bin/env python
f1=open('/Users/gtc/Desktop/work/queue/contacts.dat')
lines=f1.readlines()
f1.close()
data=[]
snode=[]
dnode=[]
starttime=[]
endtime=[]
freq=[]
for line in lines:
    vector=line.split('\t')
    snode.append(int(vector[0]))
    dnode.append(int(vector[1]))
    starttime.append(int(vector[2]))
    endtime.append(int(vector[3]))
    freq.append(int(vector[4]))
allstart=min(starttime)
allend=max(endtime)
totaltime=float(allend-allstart)
nodelabel=[]
allnode=snode+dnode
allnode.sort()
for num in allnode:
    if num in nodelabel:
        continue
    else:
        if num>max(snode):
            break
        nodelabel.append(num)
mu=[]
f2=open('/Users/gtc/Desktop/work/queue/mu.txt','w')
totalmeet=0.0
for node1 in range(1,len(nodelabel)+1):
    mumed=[]
    for node2 in range(1,len(nodelabel)+1):
        meet=0
        for slabel in range(len(snode)):
            if snode[slabel]==node1:
                if dnode[slabel]==node2:
                    meet+=1
            if snode[slabel]==node2:
                if dnode[slabel]==node1:
                    meet+=1
        totalmeet+=meet
        if meet==0:
            mumed2=1e5
        else:
            mumed2=totaltime/meet
        if node1==node2:
            mumed2=0.0
        mumed.append(mumed2)
        f2.write(str(mumed2))
        f2.write(' ')
    mu.append(mumed)
    f2.write('\n')
f2.close()
print(totalmeet/totaltime)
