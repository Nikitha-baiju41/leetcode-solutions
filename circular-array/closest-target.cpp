// Problem: Closest Target in Circular Array

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int closestTarget(vector<string>& words, string target, int startIndex) {
        int n = words.size();
        int ans = INT_MAX;

        for (int i = 0; i < n; i++) {
            if (words[i] == target) {
                int right = (i - startIndex + n) % n;
                int left = (startIndex - i + n) % n;

                int dist = min(right, left);
                ans = min(ans, dist);
            }
        }

        if (ans == INT_MAX) return -1;
        return ans;
    }
};
