#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;
int n, k, x;
bool check(int m, vector<int> &ropes)
{
    int i, s = 0;
    for (i = 0; i <= n; i++)
    {
        if (i == x)
            continue;
        s += int(ropes[i] / m);
    }
    if (s >= k)
        return true;
    return false;
}
int cut(int m, vector<int> &ropes)
{
    int i;
    if (m < 0)
        for (i = ropes[0]; i >= 1; i--)
            if (check(i, ropes))
                return i;
    if (check(ropes[m], ropes))
        for (i = ropes[m + 1]; i >= ropes[m]; i--)
            if (check(i, ropes))
                return i;
    return cut(m - 1, ropes);
}
int main()
{
    int i;
    cout << "enter the number of ropes: ";
    cin >> n;
    cout << "enter the number of same-sized ropes you want: ";
    cin >> k;
    vector<int> ropes(n + 1);
    cout << "enter the length of ropes: ";
    for (i = 0; i < n; i++)
        cin >> ropes[i];
    x = int(accumulate(ropes.begin(), ropes.end() - 1, 0) / k);
    ropes[n] = x;
    sort(ropes.begin(), ropes.end());
    x = find(ropes.begin(), ropes.end(), x) - ropes.begin();
    if (ropes[x] == ropes[x + 1])
        x++;
    cout << cut(x - 1, ropes);
    return 0;
}
