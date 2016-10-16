"""
input

1sp2sp3spnl
34sp45sp1spnl

"""
#--------------------------------------------------------------------
import math
min_sup=0.2

#min_sup=0.04
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
    print i,data_fre[i],sup_fre


for i in range(max_item+1):
    
    if data_fre[i]>=sup_fre:
        L[1].append([i])
        
    if data_fre[i]:
        C[1].append([i])

print 'C[1] = ',C[1]
print 'L[1] = ',L[1]

def L_C(length):

    print length

    if length<=1:
        return
    
    if len(L[length-1])<=1:
        return 
    L_len=len(L[length-1])
    
    for i in range(L_len):

        
        u=L[length-1][i]
        u=set(u)
        
        j=i+1
        while j<L_len:

            
            
            temp=[]
            v=data_pointer[j]
            v=set(v)
            print i,u
            print j,v
            #u_and_v_set=u.intersection(v)
            #uv_len=len(u_and_v_set)
            
            if length==2:
                
                #print length
                temp=[i]+[j]
                C[length].append(temp)
                u_and_v_set=u.intersection(v)
                uv_len=len(u_and_v_set)
                if uv_len>=sup_fre:
                    L[length].append(temp)
                    
                
            else:
                
                #print length
                ax=L[length-1][i]
                ay=L[length-1][j]
                
                
                x=ax.pop()
                y=ay.pop()
                
                if x!=y and ax==ay :
                    temp=ax+[x]+[y]
                    
                    x_set=set(data_pointer[x])
                    y_set=set(data_pointer[y])

                    x_and_y_set=x_set.intersection(y_set)
                
                    xy_fre=len(xy_set)
                    if xy_fre>=sup_fre:
                    
                        C[length].append(temp)
                    
                        u=set(u)
                        v=set(v)
                        u_and_v_set=u.intersection(v)#u set == v set
                    
                        uv_and_xy_set=u_and_v_set.intersection(x_and_y_set)
                        uvxy_len=len(uv_and_xy_set)
                
                        if uvxy_len>=sup_fre:
                            L[length].append(temp)
                    
                    
            j+=1


print max_item
for i in range(1,max_item):
    L_C(i)
    print '-------------------------------------------',i
    if len(C[i]):
    
        print 'C_',i,' = ',C[i]
        print 'L_',i,' = ',L[i]
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
'''
