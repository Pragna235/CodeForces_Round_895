import math

def min_moves(a,b,c):
    mini = min(a,b)
    maxi=max(a,b)
    moves=0
    
    if mini==maxi:
        return 0
    while(mini<maxi):
        water = min(c,maxi-mini)
        moves+=1
        mini+=water
        maxi-=water
    return moves
    
for t in range(int(input())):
    a,b,c=map(int,input().split())
    print(min_moves(a,b,c))
