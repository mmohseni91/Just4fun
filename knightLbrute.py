# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:31:06 2019

@author: Mohammad
"""

def isInBoard (a,b,n):
    '''
        checks if a gven position exists in 
        the n*n board
        
        inputs:
            a: x component of position
            b: y component of position
            n: width of the square board    
    '''
    if (a < n and b < n):
        if (a > -1 and b > -1):
            return True
    return False

def possible_moves (a,b,i,j):
    
    if (i == j):
        arr = [[a + i,b + j],
               [a - i,b + j],
               [a + i,b - j],
               [a - i,b - j]]
    else:
        arr = [[a + i,b + j],
               [a - i,b + j],
               [a + i,b - j],
               [a - i,b - j],
               [a + j,b + i],
               [a - j,b + i],
               [a + j,b - i],
               [a - j,b - i]]
    return arr

def move(n,x,y):
    '''
        find the minumum number of moves to take knight 
        to the last cell of the board, i.e. position [n,n]
        
        inputs:
            x: number of moves in width
            y: number of moves in length
            n: width of the square board    
            
        output:
            - The minimum number moves required to the
            last element of board, i.e. cell at [n,n]
            - returns 1 if x = n and y = n
            - returns -1 if no path found
            - always integer is returned            
    '''
    
    visited = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(0)                
        visited.append (aux)
    # mark the starting cell as visited 
    visited[0][0] = 1
    nummove = 0
    step_to_end = []
    path_record = []
    ## initial moves
    moves = possible_moves(0,0,x,y)

    aux_arr = []
    
    ## take the first step first!
    for i in range(len(moves)):
        if (isInBoard(moves[i][0],moves[i][1],n)):
            if (visited[moves[i][0]][moves[i][1]] == 0):
                if (moves[i][0] == n-1 and moves[i][1] == n-1):
                    return 1
                else:
                    aux_arr.append(moves[i])
                    visited[moves[i][0]][moves[i][1]] = 1
                    
    path_record.append(aux_arr)     
    while True:
        auxarr = []
        for i in range(len(path_record[nummove])):
            k = path_record[nummove][i][0]
            l = path_record[nummove][i][1]
            moves = possible_moves(k,l,x,y)
            print(moves)
            for j in range(len(moves)):
                if (isInBoard(moves[j][0],moves[j][1],n)):
                    if (visited[moves[j][0]][moves[j][1]] == 0):
                        if (moves[j][0] == n-1 and moves[j][1] == n-1):
                            step_to_end.append(nummove+2)
                        else:
                            visited[moves[j][0]][moves[j][1]] = 1
                            auxarr.append(moves[j])
        ## exit if there is no next move
        if (len(auxarr) == 0):
            break
        ## otherwise go to next move
        else:
            path_record.append(auxarr)
            nummove = nummove + 1
    if (len(step_to_end) == 0):
        return -1
    else:
        return min(step_to_end)