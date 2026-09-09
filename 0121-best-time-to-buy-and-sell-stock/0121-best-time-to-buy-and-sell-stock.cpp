class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> maxArray(prices.size());
        maxArray[0] = prices[0];
        int profit=0;
        for(int i=1;i<prices.size();i++){
            maxArray[i] = min(maxArray[i-1],prices[i-1]);
            profit = max(profit,prices[i]-maxArray[i]);
        }
        return profit;
    }
};
