# l is a stated list, v is value
#this function takes a list and a value and returns true if the value is in the list, and false if it isn't
def binary_search(l,v):
    start=0
    end=len(l)-1
    while start+1 < end :
        mid=(start+end)/2
        if l[mid]==v:
            return True
        elif l[mid]<v:
            start=mid
        elif l[mid]>v:
            end=mid
    return False


print binary_search([1,3,5,6,9,18,34,56,135],2)









