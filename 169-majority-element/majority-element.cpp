class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int middle = nums[nums.size()/2];
        return middle;
        
    }
};