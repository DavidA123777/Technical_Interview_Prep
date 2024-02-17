#include <unordered_map>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // Naive solution is to use a double for loop and iterate through the rest of the array starting from that element all the way to the end
        // Another solution would be to use a hash map to store key-value pairs (number, index). This can tell us if we have seen this element already or not.
    std::unordered_map<int,int> umap;
    for (int i = 0; i < nums.size(); i++){
        if (umap.find(nums[i]) != umap.end()){
            return true;
       }
         umap[nums[i]] = i;

    }
    return false;

    }
};
