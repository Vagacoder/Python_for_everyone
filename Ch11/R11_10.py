## R11.10
# revised the Towers of Hanoi puzzle.
# show how many total steps taken to solve puzzle
# the step of move(n) = step of move(n-1) + 1 + step of move(n-1)
#   = 1 + 2 * step of move(n-1)
def main() :
    NDISKS = 4
    towers = [list(range(1, NDISKS + 1)), [], []]
    print(towers)
    print(move(towers, NDISKS, 0, 2))

## Moves a pile of disks from one peg to another and displays the movement.
#  @param towers a list of three lists of disks
#  @param disks the number of disks to move
#  @param fromPeg the peg from which to move the disks
#  @param toPeg the peg to which to move the disks
#  @return the step taken so far
def move(towers, disks, fromPeg, toPeg) :
    step = 0
    if disks > 0 :
        other = 3 - fromPeg - toPeg
    
        step += move(towers, disks - 1, fromPeg, other)
        
        diskToMove = towers[fromPeg].pop()
        towers[toPeg].append(diskToMove)
        print(towers)
        step += 1
        
        step += move(towers, disks - 1, other, toPeg)
        
    return step

# Start the program.
main()
