#include <iostream>  
using namespace std;

void printname(char *name)  
{  
    cout << "Name:" << &name << endl;  
}  
  
int main()  
{  
    char x[30];  // array declaration  
    void (*ptr)(char*);  // function pointer declaration  
    ptr=printname;  // storing the address of printname in ptr.  
    cout << "Enter name: " << endl;
    cin>>x;
    for(int i=0; i<30; i++){
        cout << *(x+i);
    }
    cout << endl;
    //cout<<x<<endl;  
    ptr(x);  // calling printname() function  
   return 0;  
}  
