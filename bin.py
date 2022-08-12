def bin(high,low,key,a):
    mid=int((high+low)/2)
    if (a[mid]==key):
        return mid
    else:
        if(a[mid]>key):
            return bin(mid-1,low,key,a)
        else:
            return bin(high,mid+1,key,a)

a=[1,2,3,4,5,6,7,8,9,10]
key=int(input("ENTER THE KEY VALUE:"))
if key not in a:
    print(f"{key} IS NOT PRESENT IN THE LIST")
else:
    print(f"{key} IS PRESENT IN THE LIST")
    inde=bin(len(a),0,key,a)
    print(f"THE POSIITION OF {key} IS {inde}")
