class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> newnums;
        newnums.push_back(nums [0]);
        for(int i=1;i<nums.size();i++){
            if (nums[i]!= newnums[newnums.size()-1]){
                newnums.push_back(nums[i]);
            }
        }
        nums = newnums;
        int k=newnums.size();
        return k;

        
    }
};