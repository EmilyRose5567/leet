class Solution {
public:
    int jump(vector<int>& nums) {
        int jumps = 0;
        int currentEnd=0;
        int maxReach = 0;
        for(int i=0;i<nums.size()-1;i++){
            if (maxReach<nums[i]+i){maxReach = nums[i]+i;}
            if(i==currentEnd){
                jumps++;
                currentEnd=maxReach;
            }
        }
        return jumps;
        
    }
};

        