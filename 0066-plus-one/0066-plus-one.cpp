class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        int carry=0;
        int n = digits.size();
        vector<int> tmp(n,0);
        tmp[0]=1;
        reverse(digits.begin(),digits.end());
        for(int i=0;i<n;i++){
            int sum=0;
            sum = (digits[i]+ tmp[i] + carry)%10;
            carry = (digits[i]+ tmp[i] + carry)/10;
            digits[i] = sum;
        }
        if(carry != 0){
            digits.push_back(carry);
        }
        reverse(digits.begin(),digits.end());
        return digits;
    }
};