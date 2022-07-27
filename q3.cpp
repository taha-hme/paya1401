#include <iostream>
using namespace std;
int execution(int x)
{
    if (x == 1)
        return 1;
    if (x % 2 == 0)
        return 2 * execution(x / 2) - 1;
    return 2 * execution(int(x / 2)) + 1;
}
int main()
{
    int n;
    cout << "enter the number of people: ";
    cin >> n;
    cout << execution(n);
    return 0;
}