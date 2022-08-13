#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<vector<int>> checked;
int game(vector<int> boxes)
{
    int i, j;
    for (i = 0; i < boxes.size(); i++)
        if (boxes[i] == 0)
        {
            boxes.erase(boxes.begin() + i);
            i--;
        }
    sort(boxes.begin(), boxes.end());
    if (boxes.size() == 1)
        return 1;
    if (boxes.size() == 2)
    {
        if (boxes[0] == boxes[1])
            return 2;
        else
            return 1;
    }
    if (boxes.size() == 3)
    {
        if (boxes[0] == boxes[1] || boxes[1] == boxes[2])
            return 1;
        if (boxes[0] == 1)
        {
            if (boxes[1] % 2 == 0 && boxes[1] + 1 == boxes[2])
                return 2;
            else
                return 1;
        }
    }
    vector<vector<int>>::iterator it = find(checked.begin(), checked.end(), boxes);
    if (it != checked.end())
        if (checked[it - checked.begin() + 1][0] == 1)
            return 1;
        else
            return 2;
    for (i = 0; i < boxes.size(); i++)
    {
        if (i != 0)
            if (boxes[i] == boxes[i - 1])
                continue;
        for (j = boxes[i]; j > 0; j--)
        {
            boxes[i] -= j;
            if (game(boxes) == 2)
            {
                boxes[i] += j;
                checked.push_back(boxes);
                checked.push_back({1});
                return 1;
            }
            boxes[i] += j;
        }
    }
    checked.push_back(boxes);
    checked.push_back({2});
    return 2;
}
int main()
{
    int n, i, x;
    cout << "enter the number of boxes: ";
    cin >> n;
    vector<int> boxes;
    cout << "enter the number of candies: ";
    for (i = 0; i < n; i++)
    {
        cin >> x;
        boxes.push_back(x);
    }
    if (game(boxes) == 1)
        cout << "Delbakhte";
    else
        cout << "Delshekaste";
    return 0;
}
