#  Remove Element (Two Pointer | Easy)

##  Problem

Given an array `nums` and a value `val`, remove all occurrences of `val` in-place and return the number of remaining elements.

---

## Topic

* Array
* Two Pointer Technique

---

##  Approach

We use two pointers:

* One pointer (`i`) to traverse the array
* Another pointer (`k`) to store valid elements

If the current element is not equal to `val`, we place it at index `k`.

---
##  Steps / Algorithm

1. Initialize `k = 0`
2. Traverse the array using `i`
3. If `nums[i] != val`:

   * Assign `nums[k] = nums[i]`
   * Increment `k`
4. Return `k`

---

##  Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

##  Code

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
};
```

---

##  Key Learning

* Two-pointer technique helps modify arrays in-place
* Efficient solution without extra memory
