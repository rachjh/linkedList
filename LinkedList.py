#Rachel Herman


    #freelist setup
    #myList Setup
        #exps - delete 1st or last with only one item
    #print all values in myList
    #find a certain value in myList
    #add a node to front of myList
    #add a node to end of myList
    #delete first item from the list
    #delete last item from the list
    #add new item after specified item
    #add new item before specified item
    #delete a specified item from the middle of the list


data = []
pointer = []
freeListLoc = 0
myListLoc = None

def main():
    
    freeListSetup()  
    myListSetup(26)
    findSpecificValue(26)
    addNodeToFront(27)
    addNodeToFront(29)
    addNodeToFront(28)
    addNodeToEnd(30)
    deleteFirstItem()
    addAfterSpecificValue(26, 3)
    addBeforeSpecificValue(27, 31)
    deleteSpecificValueMiddle(3)
    printAllListValues()
    printLists()
    
    
def printLists():
    print("DATA:    ", data)
    print("POINTER: ",pointer)

def freeListSetup():
    dataSetup()
    pointerSetup()

def dataSetup():
    global data
    while (len(data) < 26 ):
        data.append(None)
    
def pointerSetup():
    global pointer
    x = 1 #this is the first pointer
    while (len(pointer) < 25 ): 
        pointer.append(x)
        x+=1
    
    lastIndexInPointer = (len(pointer) - 1)
    pointer[lastIndexInPointer] = -1 #the last index in list pointer
    
''

def myListSetup(x): #in slides- Create a New List #creates a list consisting of one node.
    global myListLoc
    global freeListLoc
    myListLoc = freeListLoc #myListLoc has taken the first spot in the free list
    freeListLoc = pointer[myListLoc]
    
    data[myListLoc] = x
    pointer[myListLoc] = -1
    
''

def printAllListValues():
    print('\nPrinting all values:')
    currentLoc = myListLoc
    
    while (pointer[currentLoc] != -1): #pointer at first index in pointer
        print(data[currentLoc])
        
        currentLoc = pointer[currentLoc] #sets the currentLoc to the index that the pointer sends to.

    #once the pointer is -1, print it's data and finish printing
    print(data[currentLoc])
    print("myList has ended\n")


''

def findSpecificValue(desiredValue):
    currentPointer = myListLoc #pointer starts at beginning of myList
    found = False
    
    while (found == False): #cycle will stop if it's found or a -1 is hit
        if data[currentPointer] == desiredValue: #if data in this index is desired, then print and set true
            print("The value you were looking for: ", desiredValue, "is in location:", currentPointer)
            found = True
            
        else: #otherwise set the currentPointer to the pointer in the index in the pointer list
            currentPointer = pointer[currentPointer] #becomes the next item in the list
            
        if (currentPointer == -1):
            break
        
    if (found == False): #after whole cycle if it left while loop without finding data, then not in list
        print("Your value was not in the list.")
    
''    
def addNodeToFront(newValue):
    global freeListLoc
    global myListLoc

    currentPointer = freeListLoc #getting the index of the first node in the pointer list
    
    freeListLoc = pointer[currentPointer] #setting freeListLoc to begin at the next node in freeList which this pointer pointed to
    
    data[currentPointer] = newValue
    pointer[currentPointer] = myListLoc #myListLoc points to the previous first index of myList
    
    myListLoc = currentPointer #currentPointer is the index that the detached node is in (which is now beginning of myList)


''
def addNodeToEnd(newValue):
    global freeListLoc
    
    #find end of myList
    currentLoc = myListLoc
    
    while (pointer[currentLoc] != -1):
        currentLoc = pointer[currentLoc]
        
    #currentLoc is now the index of the last index in myList
    endOfMyList = currentLoc
    
    #detach a node from freeList
    currentLoc = freeListLoc #index of beginning of freeList
    
    freeListLoc = pointer[freeListLoc] #start freeList from next pointer
    
    #set values in the detached node
    data[currentLoc] = newValue
    pointer[currentLoc] = -1
    
    #attach to myList
    pointer[endOfMyList] = currentLoc
''    
def deleteFirstItem():
    global myListLoc
    global freeListLoc
    
    firstNode = myListLoc #index of first node
    
    myListLoc = pointer[myListLoc]
    
    data[firstNode] = None
    pointer[firstNode] = freeListLoc
    
    freeListLoc = firstNode
''    
def deleteLastItem():
    global freeListLoc
    
    currentLoc = myListLoc
    
    while (pointer[currentLoc] != -1):
        previousLoc = currentLoc
        currentLoc = pointer[currentLoc]
        
    #currentLoc is now the index of the last index in myList
    endOfMyList = currentLoc
    
    data[endOfMyList] = None
    pointer[endOfMyList] = freeListLoc
    
    freeListLoc = endOfMyList
    
    pointer[previousLoc] = -1
    
def addAfterSpecificValue(specifiedValue, newValue):
    global freeListLoc
    
    currentPointer = myListLoc #pointer starts at beginning of myList
    found = False
    specifiedValueLoc = None

    while (found == False): #cycle will stop if it's found or a -1 is hit
        if data[currentPointer] == specifiedValue: #if data in this index is desired, then print and set true
            specifiedValueLoc = currentPointer
            found = True
            
        else: #otherwise set the currentPointer to the pointer in the index in the pointer list
            currentPointer = pointer[currentPointer] #becomes
            
        if (currentPointer == -1):
            break
        
    if (found == False): #after whole cycle if it left while loop without finding data, then not in list
        print("Your value was not in the list.")
        
    else: #was in the list
        if (pointer[specifiedValueLoc] == -1): #if it's the last item
            addNodeToEnd(newValue)
        else: #if the specified value is NOT the last one
            nextItemLoc = pointer[specifiedValueLoc] #the index of node after the specified one

            #detach a node from freeList
            currentLoc = freeListLoc #index of beginning of freeList
            
            freeListLoc = pointer[freeListLoc] #start freeList from next pointer

            #attach to myList
            pointer[specifiedValueLoc] = currentLoc
            
            #set values in the detached node
            data[currentLoc] = newValue
            pointer[currentLoc] = nextItemLoc
    
''
def addBeforeSpecificValue(specifiedValue, newValue):
    global freeListLoc
    
    currentPointer = myListLoc #pointer starts at beginning of myList
    found = False
    specifiedValueLoc = None

    while (found == False): #cycle will stop if it's found or a -1 is hit
        if data[currentPointer] == specifiedValue: #if data in this index is desired, then print and set true
            specifiedValueLoc = currentPointer
            found = True
            
        else: #otherwise set the currentPointer to the pointer in the index in the pointer list
            previousItemLoc = currentPointer

            currentPointer = pointer[currentPointer] #becomes

            
        if (currentPointer == -1):
            break
        
    if (found == False): #after whole cycle if it left while loop without finding data, then not in list
        print("Your value was not in the list.")
        
    else: #was in the list
        if (specifiedValueLoc == myListLoc): #if it's the first item
            addNodeToFront(newValue)
            
        else: #if the specified value is NOT the first one
            
            #detach a node from freeList
            currentLoc = freeListLoc #index of beginning of freeList
            
            freeListLoc = pointer[freeListLoc] #start freeList from next pointer

            #attach to myList
            pointer[previousItemLoc] = currentLoc
            
            #set values in the detached node
            data[currentLoc] = newValue
            pointer[currentLoc] = specifiedValueLoc

def deleteSpecificValueMiddle(specifiedValue):
    global freeListLoc
    
    currentPointer = myListLoc #pointer starts at beginning of myList
    found = False
    specifiedValueLoc = None

    while (found == False): #cycle will stop if it's found or a -1 is hit
        if data[currentPointer] == specifiedValue: #if data in this index is desired, then print and set true
            specifiedValueLoc = currentPointer
            found = True
            
        else: #otherwise set the currentPointer to the pointer in the index in the pointer list
            previousItemLoc = currentPointer
            currentPointer = pointer[currentPointer]
            
        if (currentPointer == -1):
            break
        
    if (found == False): #after whole cycle if it left while loop without finding data, then not in list
        print("Your value was not in the list.")
        
    else: #was in the list
        if (pointer[specifiedValueLoc] == -1): #if it's the last item
            deleteLastItem()
        elif(specifiedValueLoc == myListLoc):
            deleteFirstItem()
        else: #if the specified value is NOT the first or last one
             pointer[previousItemLoc] = pointer[specifiedValueLoc]
             
             data[specifiedValueLoc] = None
             pointer[specifiedValueLoc] = freeListLoc
             
             freeListLoc = specifiedValueLoc
       
    
main()