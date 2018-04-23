// #include <iostream>
// using namespace std;
// template <class T>
// void chang(T&a, T&b){
//   T t;
//   t = a;
//   a = b;
//   b = t;
// }
// int main(){
//   double x = 2.3, y = 4.7;
//   int m = 3, n = 5;
//   chang(x, y);
//   cout << "X = " << x << endl << "Y = " << y << endl;
//
//   chang(m, n);
//   cout << "M = " << m << endl <<  "N = " << n << endl;
// }

// #include <iostream>
// using namespace std;
// template <class type1, class type2>
// void chang(type1 x, type2 y){
//   cout << "x = " << x << endl;
//   cout << "y = " << y << endl;
// }
// int main(){
//   chang(10, 'g');
//   chang(2.5, 10);
// }

// Перегрузка шаблона функции(явная специализация функции)

// При перегрузке шаблона функции создается отдельный вариант функции, с явным указыванием аргументов.

// #include <iostream>
// using namespace std;
// template <class x>
// void change(x&a, x&b){
//   x t;
//   t = a;
//   a = b;
//   b = t;
// }
// void change(int&a, int&b){
//   int t;
//   t = a;
//   a = b + 1;
//   b = t + 1;
// }
// int main(){
//   double x = 2.3, y = 4.7;
//   int m = 5, n = 8;
//
//   change(x, y);
//   cout << "x = " << x << endl;
//   cout << "y = " << y << endl;
//   change(m, n);
//   cout << "m = " << x << endl;
//   cout << "n = " << y << endl;
// }

// Шаблон класса
// Классы в которых тип данных передается как формальный параметр называется шаблоном класса.
//Синтаксис шаблона класса
// #include <iostream>
// using namespace std;
//
// template <class Any>
// class Classic{
//   Any val;
// public:
//   Classic(Any m):val(m){}
//   void set(Any m){
//     val = m;
//   }
//   void show(){
//     cout << "value = " << val << endl;
//   }
// };
//
// int main(){
//   Classic <int> obj(5);
//   obj.show();
//   obj.set(3);
//   obj.show();
//   Classic <char> b('x');
//   b.show();
//   b.set('z');
//   b.show();
// }

// Перегрузка шаблона класса

// #include <iostream>
// using namespace std;
//
// template <class Any>
// class Classic{
//   Any val;
// public:
//   Classic(Any m):val(m){}
//   void set(Any m){
//     val = m;
//   }
//   void show(){
//     cout << "value = " << val << endl;
//   }
//
// };
//
// template <>
// class Classic <int>{
// public:
//   int value;
//   Classic():value(5){}
// };
//
// int main(){
//   Classic <int> a;
//   cout << "A = " << a.value << endl;
//   a.value = 3;
//   cout << "A = " << a.value << endl;
//
//   Classic <char> a('3');
//   a.show();
//   a.set('2')
//   a.show();
//
// }

#include <iostream>
using namespace std;

template <class Any = int>
class Classic{
  Any val;
public:
  Classic(Any m):val(m){}
  void set(Any m){
    val = m;
  }
  void show(){
    cout << "value = " << val << endl;
  }

};

int main() {
  Classic <> a(5);
  a.show();
  a.set(3);
  a.show();

  Classic <char> a('X');
  a.show();
  a.set('Y');
  a.show();
  a.set('Z');
  a.show();
  return 0;
}
