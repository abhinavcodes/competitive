/* https://www.hackerrank.com/challenges/staircase */

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n,i,j,z;
    cin >> n;
    int count = n-1;
    for(i=0;i<n;i++,count--)
    {
        for(j=0;j<count;j++)
        {
            cout<<" ";
        }
        for(z=0;z<=i;z++)
        {
            cout<<"#";
        }
        cout<<endl;
    }
    return 0;
}
