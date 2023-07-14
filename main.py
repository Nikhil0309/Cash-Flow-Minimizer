def insert_in_graph(j): 
    global graph_initial
    i=1
    #print("Enter y if yes n if no:")
    print("Enter information how much you owe to every other in following,{} ".format(graph_initial[j][0]))
    while(True):
        if(i==len(graph_initial)):
            break

        if(i==j):
            i=i+1
            graph_final[j].append(0)
            graph_initial[j].append(0)
            continue
        b=input("Do you owe {0} money : ".format(graph_initial[i][0]))
        if(b=="y"):
            f=int(input("What is the amount : "))
            i=i+1
            graph_initial[j].append(f)
            graph_final[j].append(0) #Making a n*n matrix called graph_final with everything 0
        elif(b=="n"):
            graph_initial[j].append(0)
            graph_final[j].append(0)
            i=i+1
        else:
            print("Not vaid input")


def add_debits(i):
    global graph_initial
    m=0
    for j in range(1,len(graph_initial)):
        if(j==i):
            continue
        if(graph_initial[i][j]!=0):
            m=m+graph_initial[i][j]
    return m

def money_involved():
    global graph_initial
    global graph_credit
    global graph_debit
    for i in range(1,len(graph_initial)):
        c=0
        for j in range(1,len(graph_initial)):
            if(graph_initial[j][i]!=0):
                c=c+graph_initial[j][i]

        m=add_debits(i)
        c=c-m
        if(c>0): 
            graph_credit[i].append(c)
            graph_debit[i].append(0)
        if(c<0):
            d=-c
            graph_credit[i].append(0)
            graph_debit[i].append(d)
        if(c==0):
            graph_credit[i].append(0)
            graph_debit[i].append(0)


def final_graph():
    global graph_initial
    global graph_credit
    global graph_debit
    maxcredit=calculation()

def calculation():
    global graph_initial
    global graph_credit
    global graph_debit
    global graph_final
    v=1
    m=1
    while(True):
        v=0
        c=graph_credit[1][0]
        l=1
        for i in range(1,len(graph_credit)):
            if(graph_credit[i][1]>v):
                v=graph_credit[i][1]
                c=graph_credit[i][0]
                l=i

        m=0
        k=1
        n=graph_debit[1][0]
        for i in range(1,len(graph_debit)):
            if(graph_debit[i][1]>m):
                m=graph_debit[i][1]
                n=graph_debit[i][0]
                k=i
        if(m==0 and v==0):
            break
        if(v>m):
            v=v-m
            graph_final[k][l]=m
            graph_credit[l][1]=v
            graph_debit[k][1]=0
        else:
            m=m-v
            graph_final[k][l]=v
            graph_credit[l][1]=0
            graph_debit[k][1]=m

print("***WELCOME TO CASH FLOW MINIMIZER***")
n=int(input("Total people involved :"))
graph_initial=[[]]
list_name=[]
graph_credit=[[]]
graph_debit=[[]]
graph_final=[[]]
stackcr=[]
stackde=[]

for i in range(0,n):
    c=input("Enter name of person {} :".format(i+1))
    graph_initial.append([c]) #initialising all graphs to 0
    graph_credit.append([c])
    graph_debit.append([c])
    graph_final.append([c])

print("NOTE: 'y' for yes and 'n' for no ")

for j in range(1,n+1):
    insert_in_graph(j) 

money_involved()
final_graph()

#print(list(graph_final))
#print(graph_initial)

gr = graph_initial
print("\nInitial Transactions: ")
k=1
for i in range(1,len(gr)):
    for j in range(0,len(gr)):
        if(j==0):
            continue
        else:
            if(gr[i][j]!=0):
                print("{}. {} owes {} Rs to {}".format(k,gr[i][0],gr[i][j],gr[j][0]))
                k+=1

k=1
gr = graph_final
print("\nFinal Transactions:")
for i in range(1,len(gr)):
    for j in range(0,len(gr)):
        if(j==0):
            continue
        else:
            if(gr[i][j]!=0):
                print("{}. {} owes {} Rs to {}".format(i,gr[i][0],gr[i][j],gr[j][0]))
                k+=1

'''
print("\nInitially :")
gr=graph_initial
for i in range(1,len(gr)):
    for j in range(0,len(gr)):
        if(j==0):
            continue
        else:
            if(gr[i][j]!=0):
                print("{} owes {} Rs to {}".format(gr[i][0],gr[i][j],gr[j][0]))
            
print("\nFinally :")
gr=graph_final
for i in range(1,len(gr)):
    for j in range(0,len(gr)):
        if(j==0):
            continue
        else:
            if(gr[i][j]!=0):
                print("{} owes {} Rs to {}".format(gr[i][0],gr[i][j],gr[j][0]))'''
