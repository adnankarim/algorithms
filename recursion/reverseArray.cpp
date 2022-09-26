// Online C++ compiler to run C++ program online
// Online C++ compiler to run C++ program online
// TC: O(n/2) and space Complexity O(n/2) internal stack space
#include <iostream>
using namespace std;
void reverseArray(int i, int arr[],int n){
    if (i>=n/2){
        return;
    }
    swap(arr[i],arr[n-1-i]);
    reverseArray(i+1,arr,n);
}
int main() {
    // Write C++ code here
    
    int arr [] ={1,2,3,4};
    reverseArray(0,arr,4);
    for (int i=0;i<4;i++)
        cout<<arr[i];
    return 0;
}