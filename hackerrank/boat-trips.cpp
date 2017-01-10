#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n,c,m,i;
    cin>>n;
    cin>>c;
    cin>>m;
    int arr[n];
    for(i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    int e = sizeof(arr)/sizeof(arr[0]);
    sort(arr, arr+e);
    if(arr[n-1] <= (c*m))
    {
        cout<<"\nYes\n";
    }
    else
    {
        cout<<"\nNo\n";
    }
    return 0;
}
