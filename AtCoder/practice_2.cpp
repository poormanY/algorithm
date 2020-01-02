// https://atcoder.jp/contests/practice/tasks/practice_2
#include<iostream>
using namespace std;

int main()
{
  int N,Q,i,j;
  // get two integers
  cin >> N >> Q;

  string s;
  for (i=0; i<N; i++) {
    s += (char)('A' + i);
  }

  for (i=0; i<N; i++) {
    for (j=0; j<N-1; j++) {
      cout << "? " << s[j] << " " << s[j+1] << endl;
      char ans;
      cin >> ans;
      if (ans == ">") {
        swap(s[j], s[j+1]);
      }
    }
  }
  cout << "! " << s << endl;
  return 0;
}
