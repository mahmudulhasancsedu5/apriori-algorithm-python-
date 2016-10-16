import math
min_sup=0.2
min_conf=0.7
#---------------------------------input file processing------------
inputFile=open('input.txt','r')
outputFile=open('output.txt','w')

data=inputFile.readlines()

print data[0]

sup_fre=int(math.ceil(len(data)*min_sup))


linear_list=data

data_array=[]
i=0
for line in data:
    #print line
    data_array.append(line.replace('\n','').split(' '))
    i+=1

# convert item from string to int
# data list will contain the data bse vector (TID--->itemset)
i=0
for line in data_array:
    data[i]=list(set([int(x) for x in line]))
    i+=1
#print data

linear_data_list=[]# contain all the data of the dataset
for x in data:
    linear_data_list+=x


#print linear_data_list
#print "----------------------"
item_list=list(set(linear_data_list))#contain all the unique item of the dataset
    
#print item_list
#print "-------------------"

L=[[] for i in range(1000)]
C=[[] for i in range(1000)]


item_fre={}#1-length item frequency
for item in item_list:
    fre=linear_data_list.count(item)
    item_fre[item]=fre
    C[1].append(item)

C[1]=list(set(C[1]))
#print C[1]
for x in C[1]:
    if item_fre[x]>=sup_fre:
        L[1].append ([x])
    #print item_fre[x],x

#print L[1]

#L[1]=list(set(L[1]))#1-length frequent items set in the dataset
#---------------------------------------------------------------------------

def check_if_frequent(arr):#check in database
    #print arr

    count_arr_fre=0
    arr=set(arr)
    for trans in data:
        trans=set(trans)
        if arr.issubset(trans):
            count_arr_fre+=1;
    #print count_arr_fre,"---<sup_fre ",sup_fre
    if count_arr_fre>=sup_fre:
        return True
    else:
        return False
        
    

def L_C(length):
                
    #print length
    if len(L[length-1])==0:
        return 
    #-----------------------create C(l) from L(l-1)-----------------------
    L_prior_length=len(L[length-1])

    #print 'L_prior length = ',L_prior_length,'\n'
    
    for  i in range(L_prior_length-1):


        temp=[]
        j=i+1
        while j<L_prior_length:
            
            item_set1=[x for x in L[length-1][i]]
            
            item_set2=[x for x in L[length-1][j]]
            #print 'L(l-1)[i ] = ',L[length-1][i]
            #print 'i_set_1',item_set1
            #print 'i_set_2',item_set2
            #print i
            #print j

            if length==2:
                
                temp=item_set1+item_set2
            
                
            else:
                
            
                x=item_set1.pop()#b<------ab
                y=item_set2.pop()#c<------ac
                xy=[x]+[y]
                
                #check if xy is frequent in L(l-1)
                flag=0
                for arr in L[length-1]:
                    if xy==arr:
                        flag=1
                        break
                
                if item_set1==item_set2 and x!=y and flag==1:
                    temp=item_set1+xy#abc<----------a+(b+c)
                else:
                    temp=[]

            if len(temp):  
                C[length].append(temp)

                
            j+=1

    if len(C[length])==0:
        return
    #--------------------create L(l) from C(l)-----------
    # we finished C(l)
    # Now we will create L(l)
    

    for item_in_C in C[length]:
        #print item_in_C
        flag_ck=check_if_frequent(item_in_C)
        if flag_ck==True:
            L[length].append(item_in_C)
    
#----------------------------------execution start from here-------------------
for i in range(1,100):
    L_C(i)
    print '-------------------------------------------'
    if len(C[i]):
    
        print 'C_',i,' = ',C[i]
        print 'L_',i,' = ',L[i]
    else:
        break
        #print 'C_',i,' = ',C[i]
        #print 'L_',i,' = ',L[i]
        
    
"""
x=L_C(2)
print L[1]
print '--------------c_2-------'
print C[2]
print '--------------l_2--------'
print L[2]
x=L_C(3)
print '--------------c_3-------'
print C[3]
print '--------------l_3--------'
print L[3]
x=L_C(4)
x=L_C(5)

"""

        
        
      
        




    

    
    











