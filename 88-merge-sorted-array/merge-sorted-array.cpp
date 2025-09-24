class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

        //Combine lists
        for (int i = 0; i < n; i++) {
            nums1[m+i] = nums2[i];
        }
        
        //Order list
        sort(nums1.begin(), nums1.end());
    }
};
