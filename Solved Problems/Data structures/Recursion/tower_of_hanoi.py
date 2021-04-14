
"""
|| Problem Definition ||

The Tower of Hanoi is a puzzle where we have three rods and n unique sized disks. The three rods are - source, destination, and auxiliary.

Initally, all the n disks are present on the source rod. 
The final objective of the puzzle is to move all disks from the source rod to the destination rod using the auxiliary rod.

|| Rules of the Puzzle ||
1. Only one disk can be moved at a time.
2. A disk can be moved only if it is on the top of a rod.
3. No disk can be placed on the top of a smaller disk.

"""


def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    
    Given the number of disks num_disks as the input parameter, 
    the recursive function tower_of_Hanoi() prints the "move" steps in order to move num_disks number of disks 
    from Source to Destination using the help of Auxiliary rod.
    """
    
    tower_of_hanoi_output(num_disks, 'S', 'A', 'D')
    
    
def tower_of_hanoi_output(num_disks, source, auxiliary, destination):
    
    if num_disks == 0:
        return
    
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return
    
    tower_of_hanoi_output(num_disks - 1, source, destination, auxiliary)
    print("{} {}".format(source, destination))
    
    tower_of_hanoi_output(num_disks - 1, auxiliary, source, destination)
    
        
