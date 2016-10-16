"""
input

1sp2sp3spnl
34sp45sp1spnl

"""
#--------------------------------------------------------------------
import math
min_sup=0.2

#min_sup=0.01
min_conf=0.7
#---------------------------------input file processing------------
#inputFile=open('T10I4D100K.dat.txt','r')
inputFile=open('input.txt','r')
outputFile=open('output.txt','w')

data=inputFile.readlines()

print data[0]

sup_fre=int(math.ceil(len(data)*min_sup))


linear_list=data

L=[[] for i in range(1000)]
C=[[] for i in range(1000)]
data_fre=[]
data_pointer=[[] for i in range(1000)]
item_set=[]

data_array=[]
max_item=-1
i=0

for line in data:
     
    data_array.append(line.replace('\n','-').split(' '))
    if '-' in data_array[i]:
        data_array[i].remove('-')
        flag=0
    for val_str in data_array[i]:

        item=int(val_str)
        data_pointer[item].append(i)
        if item>max_item:
            max_item=item
        
    i+=1
print 'data_pointer = ',len(data_pointer)
print 'max_item = ',max_item

data_fre=[len(x) for x in data_pointer]

for i in range(max_item+1):
    if data_fre[i]>=sup_fre:
        print i,data_fre[i],sup_fre


for i in range(max_item+1):
    
    if data_fre[i]>=sup_fre:
        L[1].append([i])
        
    if data_fre[i]:
        C[1].append([i])

#print 'C[1] = ',C[1]
#print 'L[1] = ',L[1]


    

def L_C(length):

    print length

    if length<=1:
        return
    
    if len(L[length-1])<=1:
        return 
    L_len=len(L[length-1])

    print 'L_',length-1,L_len
    
    for i in range(L_len-1):
        #print i
        L_u=L[length-1][i]
    
        j=i+1
        while j<L_len:

            
            
            temp=[]
            L_v=L[length-1][j]

            
            
            
            
            if length==2:
                
                temp=L_u+L_v
                #print temp
                C[length].append(temp)
                
                L_u_trans_list=data_pointer[L_u[0]]
                L_v_trans_list=data_pointer[L_v[0]]

                L_u_trans_set=set(L_u_trans_list)
                L_v_trans_set=set(L_v_trans_list)

                L_uv_trans_set=L_u_trans_set.intersection(L_v_trans_set)
                if len(L_uv_trans_set)>=sup_fre:
                    L[length].append(temp)
                
               
                
            else:
                
                #print length
                ax=[x for x in L[length-1][i]]
                ay=[x for x in L[length-1][j]]
                #print i,ax,j,ay#-----------------------------------
                
                
                
                x=ax.pop()
                y=ay.pop()
                
                if x!=y and ax==ay :
                    #print 'ok 1'
                    temp=ax+[x]+[y]
                    temp1=[x for x in temp]
                    #print temp1
                    ab=ax

                    x=temp1.pop(0)# pop 0 indexed value
                    #print 'pop = ',x,temp1
                    
                    if temp1 in L[length-1]:
                        
                        #print 'ok = ok',temp1
                        C[length].append(temp)
                        
                    
                    
                        # find a transection set
                        
                        x_set=set(data_pointer[x])
                        y_set=set(data_pointer[y])
                        xy_set=x_set.intersection(y_set)
                
                    
                        
                        ab_trans_list=data_pointer[ab[0]]
                        ab_set=set(ab_trans_list)
                        
                        for val in ab:
                            ab_set=ab_set.intersection(set(data_pointer[val]))
                        
                    
                        abxy_set=ab_set.intersection(xy_set)
                        abxy_fre=len(abxy_set)
                
                        if abxy_fre>=sup_fre:
                            L[length].append(temp)
                    
                   
            j+=1
            


    
print max_item
for i in range(1,max_item+1):
    L_C(i)
    print '-------------------------------------------',i
    if len(C[i]):
        print 'len = ',i,len(C[i]),len(L[i])
        #print 'C_',i,' = ',C[i]
        #print 'L_',i,' = ',L[i]
        str1='\n'
        str1=str('L_'+str(i)+'   ')
        str2=str(L[i])
        str1+=str2
        str1+='\n'
        outputFile.write(str1)
        str1='\n'
        str1=str('C_'+str(i)+'   ')
        str2=str(C[i])
        str1+=str2
        str1+='\n'
        outputFile.write(str1)
        

        
        
    else:
        break
        #print 'C_',i,' = ',C[i]
        #print 'L_',i,' = ',L[i]
'''


print  'L_1',L[1]
print 'C_1',C[1]
L_C(2)

print '--------------c_2-------'
print 'C_2',C[2]
print '--------------l_2--------'
print 'L_2',L[2]

L_C(3)

print '--------------c_2-------'
print 'C_2',C[3]
print '--------------l_2--------'
print 'L_2',L[3]

'''
inputFile.close()
outputFile.close()




