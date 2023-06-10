'''def strcounter(str):N*M
    for sym in set(str):
        counter = 0
        for sub_sym in str:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)
strcounter('afaarjvb')'''

'''def strcounter(str):N**2
    for sym in str:
        counter = 0
        for sub_sym in str:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)
strcounter('afaarjvb')'''

def strcounter(str): #O(N)
    syms_counter = {}
    for sym in str:
        syms_counter[sym] = syms_counter.get(sym,0) + 1
    for sym, count in syms_counter.items():
        print(sym,count)

strcounter('avbgax')
