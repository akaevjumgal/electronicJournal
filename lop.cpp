#include<iostream>
using namespace std;
template <class T>
T sort(T * arr, int n) {
 T max = arr[0];
 for (int i = 0; i < n; i++){
   if (max < arr[i]){
     max = arr[i];
   }
 }
 for (int j = 0; j < n - 1; j++){
   for (int i = 0; i < n - 1; i++){
     if (arr[i] > arr[i + 1]){
       swap(arr[i], arr[i + 1]);
     }
   }
 }
 cout «"Max = "«max«endl;
 for (int i = 0; i < n; i++){
   cout «  arr[i] «" " ;
 }
 return 0;
}
int main(){
 int n;
 cout « "Please enter the size of the array: ";
 cin » n;
 char * arr = new char[n];
 cout « "Entre array of chars: ";
 for(int i = 0; i < n; i++){
   cin » arr[i];
 }
 sort(arr,n);
 cout « "\nPlease enter the size of the array: ";
 cin » n;
 int * arr1 = new int[n];
 cout « "Entre array of integers: ";
 for (int i = 0; i < n; i++){
   cin » arr1[i];
 }
 sort(arr1, n);
 cout « endl;
 system("pause");
 return 0;
}
