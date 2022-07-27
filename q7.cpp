#include <iostream>
#include <vector>
#include <numeric>
using namespace std;
int subtable(vector<int> questions, vector<vector<int>> &table)
{
    int i, s = 0;
    for (i = questions[0]; i <= questions[1]; i++)
        s += accumulate(table[i].begin() + questions[2], table[i].begin() + questions[3] + 1, 0);
    return s;
}
int main()
{
    int m, n, i, j, q, x;
    cout << "enter the number of rows: ";
    cin >> n;
    cout << "enter the number of columns: ";
    cin >> m;
    vector<vector<int>> table(n);
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
        {
            cin >> x;
            table[i].push_back(x);
        }
    cout << "enter the number of questions: ";
    cin >> q;
    vector<vector<int>> questions(q);
    for (i = 0; i < q; i++)
        for (j = 0; j < 4; j++)
        {
            cin >> x;
            questions[i].push_back(x - 1);
        }
    for (i = 0; i < q; i++)
        cout << subtable(questions[i], table) << endl;
    return 0;
}