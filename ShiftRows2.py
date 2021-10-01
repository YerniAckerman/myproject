from numpy import*


arr=array([

    ["1A","1B","3C","1E"],
    ["32","C8","19","15"],
    ["10","11","12","13"],
    ["14","15","16","17"]
    

])
print("\nShiftRows\nInput:\n")
print(arr)
print("\n")

def swap():
    i=0
    while i<3:
        
        a1=arr[1][0+i]
        arr[1][i+0]=arr[1][i+1]
        arr[1][i+1]=a1
        i+=1 
    print("First step:\n")
    print(arr)

def swap2():   
        
    x=0
    while x<2:
        j=0
        while j<3:
            a2=arr[2][0+j]
            arr[2][0+j]=arr[2][j+1]
            arr[2][j+1]=a2
            j+=1
        x+=1
    print("Second step:\n")
    print(arr)
def swap3():
    y=0
    while y<3:
        k=0
        while k<3:
            a3=arr[3][k+0]
            arr[3][0+k]=arr[3][k+1]
            arr[3][k+1]=a3
            k+=1
        y+=1
    print("Third step:\n")
    print(arr)
swap()
print("""""""""""""""""""""""")
swap2()
swap3()


