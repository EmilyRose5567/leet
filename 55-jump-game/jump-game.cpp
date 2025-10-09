class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0;
        bool possible = false;
        for (int i=0;i<nums.size();i++){
            if(i>maxReach){return false;}
            else{
                if(maxReach<i+nums[i]){
                    maxReach = i+nums[i];
                } 
            }
            if (maxReach>=i){possible=true;}
            
        }
        return possible;
        
    }

               
};