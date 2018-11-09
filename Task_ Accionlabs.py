def parti(arbitrarylist):
    '''Function that returns True if the list can be partitioned and False if it is not.'''
    if sum(arbitrarylist) % 2 == 0 : #if it is not a even sum then we can't divide it into 2 partitions

        listone = []#temporory partition one, Not necessary but useful to debug and optimize the function further
        listtwo = []#temporory partition two
        listonesum = 0
        listtwosum = 0

        for i in sorted(list1, reverse=True):#actual logic

            if listonesum > listtwosum:
                listtwosum += i
                listtwo.append(i)
            else:
                listonesum += i
                listone.append(i)

        if  listonesum == listtwosum:#checking if both list's sum is same or not
            return True
        else:
            return False

    else:
        return False
