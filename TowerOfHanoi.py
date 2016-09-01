# cook your code here
#Tower of Hanoi using Recursion
ctr=0;
def ToH(n,x,y,z):
    global ctr
    ctr=ctr+1;
    if n==1:
        print("Move disk from peg ",x," to peg ",z);
    else :
        ToH(n-1,x,z,y);
        print("Move disk from peg ",x," to peg ",z);
        ToH(n-1,y,x,z);

ToH(1,'A','B','C');
print("No of Iteration : ",ctr);

#Sample Input and Ouput
"""
Input : None 
Output : 
1
Move disk from peg A to peg C
No of Iteration : 1
2
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
No of Iteration : 3
3
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
No of Iteration : 7
4
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
Move disk from peg A to peg B
Move disk from peg C to peg A
Move disk from peg C to peg B
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
Move disk from peg B to peg A
Move disk from peg C to peg A
Move disk from peg B to peg C
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
No of Iteration : 15
5
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
No of Iteration : 31
6
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
Move disk from peg A to peg B
Move disk from peg C to peg A
Move disk from peg C to peg B
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
Move disk from peg B to peg A
Move disk from peg C to peg A
Move disk from peg B to peg C
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
Move disk from peg A to peg B
Move disk from peg C to peg A
Move disk from peg C to peg B
Move disk from peg A to peg B
Move disk from peg C to peg A
Move disk from peg B to peg C
Move disk from peg B to peg A
Move disk from peg C to peg A
Move disk from peg C to peg B
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
Move disk from peg A to peg B
Move disk from peg C to peg A
Move disk from peg C to peg B
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
Move disk from peg B to peg A
Move disk from peg C to peg A
Move disk from peg B to peg C
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
Move disk from peg B to peg A
Move disk from peg C to peg A
Move disk from peg C to peg B
Move disk from peg A to peg B
Move disk from peg C to peg A
Move disk from peg B to peg C
Move disk from peg B to peg A
Move disk from peg C to peg A
Move disk from peg B to peg C
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
Move disk from peg A to peg B
Move disk from peg C to peg A
Move disk from peg C to peg B
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
Move disk from peg B to peg A
Move disk from peg C to peg A
Move disk from peg B to peg C
Move disk from peg A to peg B
Move disk from peg A to peg C
Move disk from peg B to peg C
No of Iteration : 63
7 
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg C to peg B
Move disk from peg C to peg A
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
Move disk from peg A to peg B
Move disk from peg C to peg B
Move disk from peg A to peg C
Move disk from peg B to peg A
Move disk from peg B to peg C
Move disk from peg A to peg C
No of Iteration : 127
 """
