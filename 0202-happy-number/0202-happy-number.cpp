class Solution {
public:
    int squareSum(int n){
        int r=0,s=0;
        while(n){
            r = n%10;
            n/=10;
            s+=r*r;
        }
        return s;
    }
    bool isHappy(int n) {
        if(n==1){
            return true;
        }
        set<int> s;
        while(s.find(squareSum(n)) == s.end()){
            n = squareSum(n);
            s.insert(n);
        }
        if(n==1){
            return true;
        }
        return false;
    }
};
