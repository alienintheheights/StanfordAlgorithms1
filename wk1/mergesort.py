
'''
Engineering: Algorithms1 Algorithms: Design and Analysis
Stanford University online.
mergesort, runs in o(nlog(n)) time
Example:
    runmergesort([4, 1, 6, 3, 5, 2, 7, 8])

    runmergesort(readfile('IntegerArray.txt'))
Author: Andrew L
'''
import time

def merge(list_b, list_c):
    '''
    Merge Sort with split mylistersion mergesorter.
    o(n*log(n))
    :param list_b: The first split list
    :param list_c: The second split list
    :type a: list
    :type b: list
    :return: the resulting list, the number of splits
    :rtype: list, int
    '''
    i = j = 0
    list_d = []
    b_size = len(list_b)
    c_size = len(list_c)
    while i < b_size and j < c_size:
        if list_b[i] < list_c[j]:
            list_d.append(list_b[i])
            i += 1
        elif list_c[j] < list_b[i]:
            list_d.append(list_c[j])
            j += 1
    if j < c_size:
        list_d.extend(list_c[j:])
    elif i < b_size:
        list_d.extend(list_b[i:])
    return list_d

def mergesort(inlist):
    '''
    recursive mergesort function takes list and its size,
    returns number of mylistersions, along with sorted_list list.
    :param inlist: input list
    :param size_is: input size_is
    '''
    size_is = len(inlist)
    if size_is < 2:
        return inlist
    else:
        half = size_is / 2
        list_b = mergesort(inlist[:half])
        list_c = mergesort(inlist[half:])
        list_d = merge(list_b, list_c)
    return list_d

def runmergesort(inlist, echoinput=False, clock=False):
    '''
    Wrapper for recursive method
    :param inlist: input list
    :param echoinput: show list
    :param clock: time boolean
    '''
    if echoinput:
        print "sorting ", inlist[:20]
    if clock:
        start = time.clock()
    sorted_list = mergesort(inlist)
    if clock:
        end = time.clock()
        print "sort ran in ", end - start, " seconds"
    if echoinput:
        print "sorted  ", sorted_list[:20], "\n"
    return sorted_list

def readfile(fname):
    '''
    reads the file in, returns a list
    :param filename: the name of the file, duh
    '''
    with open(fname) as filehandle:
        return [int(x) for x in filehandle]


def main():
    '''
    Main for running test cases
    '''
    runmergesort([1, 2, 3, 4, 5], True)
    runmergesort([4, 1, 6, 3, 5, 2, 7, 8], True)
    runmergesort([3, 4, 6, 1, 2, 5], True)
    runmergesort([54044, 14108, 79294, 29649, 25260, 60660, 2995], True)

    print "reading in data file..."
    lines = readfile('IntegerArray.txt')
    print "read ", len(lines), " lines"
    runmergesort(lines, False, True)
    #print "brute force solution for ", mylist, "is ", bruteforce(lines)

if __name__ == "__main__":
    main()
