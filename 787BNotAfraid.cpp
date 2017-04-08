#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int main(){
  int  a, b, k, l;
  cin >> a >> b;
  map<int,int> myMap;
  for(int i=0; i<b; i++){
      cin>>k;
      int OK=0;
      for(int j=0;j<k;j++){
	cin>>l;
	if(myMap[-l]==1){
	  cout<< "YES" <<endl;
          return 0;
	}
	myMap[l]=1;
      }
      myMap.clear();
      if (OK==0){Answer=1;}
       
    }
  cout << "NO" <<endl;
  return 0;
}


