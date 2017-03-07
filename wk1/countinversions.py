
'''
Homework #1 in Engineering: Algorithms1 Algorithms: Design and Analysis
Stanford University online.
countsort inversions in o(nlog(n)) time
Example:
    inv = countsortinversions([4, 1, 6, 3, 5, 2, 7, 8])

    inv = countsortinversions(readfile('/Users/bob/Downloads/IntegerArray.txt'))
Author: Andrew L
'''
import time

def countsortsplitinv(list_b, list_c):
    '''
    Merge Sort with split inversion countsorter.
    Note this will return a sorted list!
    o(n*log(n))
    :param list_b: The first split list
    :param list_c: The second split list
    :type a: list
    :type b: list
    :return: the resulting list, the number of splits
    :rtype: list, int
    '''
    i = j = splits = 0
    list_d = []
    b_size = len(list_b)
    c_size = len(list_c)
    size_is = b_size + c_size
    while i < b_size and j < c_size:
        if list_b[i] < list_c[j]:
            list_d.append(list_b[i])
            i += 1
        elif list_c[j] < list_b[i]:
            list_d.append(list_c[j])
            j += 1
            splits += size_is / 2 - i
    if j < c_size:
        list_d.extend(list_c[j:])
    elif i < b_size:
        list_d.extend(list_b[i:])
    return list_d, splits

def countsort(inlist):
    '''
    recursive countsort function takes list and its size,
    returns number of inversions, along with sorted list.
    :param inlist: input list
    :param size_is: input size_is
    '''
    size_is = len(inlist)
    if size_is == 1:
        return inlist, 0
    else:
        half = size_is / 2
        list_b, hits_b = countsort(inlist[:half])
        list_c, hits_c = countsort(inlist[half:])
        list_d, hits_d = countsortsplitinv(list_b, list_c)
    return list_d, (hits_b + hits_c + hits_d)

def countsortinversions(inlist, echoinput=False, clock=False):
    '''
    Wrapper for recursive method
    :param inlist: input list
    :param echoinput: show list
    :param clock: time boolean
    '''
    if echoinput:
        print "running inversion countsort on ", inlist[:10]
    if clock:
        start = time.clock()
    (sorted_in, invcountsort) = countsort(inlist)
    if clock:
        end = time.clock()
        print "inversion countsort took ", end - start, " seconds"
    if echoinput:
        print "number of inversions:  ", invcountsort
    return invcountsort

def readfile(fname):
    '''
    reads the file in, returns a list
    :param filename: the name of the file, duh
    '''
    with open(fname) as filehandle:
        return [int(x) for x in filehandle]

def bruteforce(arr):
    '''
    o(n^2) solution, not advisable to run this on a large line data set
    '''
    size_is = len(arr)
    splits = 0
    for i in range(0, size_is):
        for j in range(i + 1, size_is):
            if arr[i] > arr[j]:
                splits += 1
    return splits

def main():
    '''
    Main for running test cases
    '''
    countsortinversions([1, 2, 3, 4, 5], True)
    countsortinversions([4, 1, 6, 3, 5, 2, 7, 8], True)
    countsortinversions([3, 4, 6, 1, 2, 5], True)
    countsortinversions([54044, 14108, 79294, 29649, 25260, 60660, 2995], True)

    print "\nreading in data file..."
    lines = readfile('/Users/andrew/Downloads/IntegerArray.txt')
    print "read ", len(lines), " lines"

    countsortinversions(lines, True, True)
    print "inv should be 2407905288"
    #print "brute force solution is ", bruteforce(lines)

if __name__ == "__main__":
    main()
