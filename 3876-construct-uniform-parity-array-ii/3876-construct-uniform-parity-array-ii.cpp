class Solution {
public:
    bool uniformArray(vector<int>& nums) {
        int minEven=INT_MAX;
        int minOdd = INT_MAX;
        for(auto x:nums){
            if(x<minEven && x%2==0){
                minEven=x;
            }
            else if(x<minOdd && x%2!=0){
                minOdd=x;
            }
        }
        if(minEven == INT_MAX || minOdd == INT_MAX){
            return true;
        }
        return minEven > minOdd ? true:false;
    }
};