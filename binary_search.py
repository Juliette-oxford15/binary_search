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

def simple_tests():
    print binary_search([1,3,5,6,9,18,34,56,135],2)

def test_search(lst,notlst):
    for item in lst:
        assert binary_search(lst, item)
    for item in notlst:
        assert not binary_search(lst, item)

def run_all_tests():
    test_search([0,0,1,1,2,2,3,3], [-3,1.5,100])
    test_search([1,3,5,7,12,12,15,16,100,132,223],
                [0,2,4,6,8,9,10,11,13,14,17,50,131,133,222,224])
    test_search([10], [1,112])
    test_search([], [10])
    test_search([0,10], [-2,2,20])

def main():
    run_simple_tests()
    run_all_tests()

if __name__ == '__main__':
    main()










