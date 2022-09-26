// Online C++ compiler to run C++ program online
// Online C++ compiler to run C++ program online
// TC: O(n/2) and space Complexity O(n/2) internal stack space

#include <iostream>
#include <string>
using namespace std;
void reverseString(int i, string &arr,int n){
    if (i>=n/2){
        return;
    }
    swap(arr[i],arr[n-1-i]);
    reverseString(i+1,arr,n);
}
int main() {
    // Write C++ code here
    
    string arr ="adnan";
    reverseString(0,arr,5);
    for (int i=0;i<5;i++)
        cout<<arr[i];
    return 0;
}