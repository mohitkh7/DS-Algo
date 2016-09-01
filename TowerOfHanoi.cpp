// Program for Tower of Hanoi Implementation using Recursion
#include<iostream>
using namespace std;
int ctr=0;
void ToH(int n, char x, char y, char z)
{
    if(n==1)
    {
        cout<<"Move disk from peg "<<x<<" to peg "<<z<<"\n";
        ctr++;
    }
    else
    {
        ToH(n-1,x,z,y);
        ToH(1,x,y,z);
        ToH(n-1,y,x,z);
    }
}
int main()
{
    ToH(7,'A','B','C');
    cout<<"No of Iteration : "<<ctr;
    return 0;
}  

// Sample Input and Ouput
/*
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
*/
