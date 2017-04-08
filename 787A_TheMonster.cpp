#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <algorithm>


using namespace std;


int printArray (int arg[], int length)  {
  for(int i=0; i<length; i++){
    cout << arg[i] <<"; ";
  } 
  cout<<endl;
   return 0; 
}

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main(){
  int  a, b, c,d;
    cin >> a >> b >> c >> d;
    
    if (abs(d-b) % gcd(a,c) !=0){
      cout<< "-1" <<endl;
      return 0;
	
    }else{

      while (b!=d){
	if(b>d){
	  d=d+c;
	}else{
	  b=b+a;
	}
      }     
      cout << b << endl;
    } 
    return 0;
}


