
dlist = []
def getData():
    while(True):
        data=input("please input data: ")
        if(data != 'done'):
            dlist.append(int(data))
            print(dlist)
        else:
            break

testData =[ 1, 5,8,0,2,4,6,7,6]
def selectionsort(dlist):
    #print(dlist, len(dlist))
    for i in range(len(dlist)-1):
        #print("index is ", i," ",dlist[i])
        temp=min(dlist[i+1:])
        subindex = dlist[i+1:].index(temp)
        index = i+1+ subindex
        #print("min value" , temp)
        if ( dlist[i] > temp):
   
            #dlist[dlist.index(temp)]  = dlist[i] 
            '''
            dlist[index]  = dlist[i] 
            dlist[i] = temp
            '''
            dlist[i],dlist[index]=temp, dlist[i] 
            print(dlist)
    print("result is below ---")
    print(dlist)

if __name__ == "__main__":
    selectionsort(testData)
    #getData()        
    #selectionsort(dlist)
