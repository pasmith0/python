#!/usr/bin/python

import sys
from copy import deepcopy

def main():
    
    d = {'x': 1, 'y': 2, 'z': 3}
    print( "d: ")
    for key in d:
        print ' [', key, ']=', d[key]

    e = d
    print( "e: ")
    for key in e:
        print ' [', key, ']=', e[key]

    print( "e after changing e[x]: ")
    e['x'] = 4
    for key in e:
        print ' [', key, ']=', e[key]

    print( "d after changing e[x]: ")
    for key in d:
        print ' [', key, ']=', d[key]

    # now with deepcopy
    d = {'x': 1, 'y': 2, 'z': 3}
    print( "d: ")
    for key in d:
        print ' [', key, ']=', d[key]

    e = deepcopy(d)
    print( "e: ")
    for key in e:
        print ' [', key, ']=', e[key]

    print( "e after changing e[x]: ")
    e['x'] = 4
    for key in e:
        print ' [', key, ']=', e[key]

    print( "d after changing e[x]: ")
    for key in d:
        print ' [', key, ']=', d[key]


if __name__ == "__main__":
    main()
   

