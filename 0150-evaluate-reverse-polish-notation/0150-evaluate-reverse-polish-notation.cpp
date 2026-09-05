class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for(auto x: tokens){
            if(x == "+" || x== "-" || x== "*" || x== "/"){
                int x2=st.top();
                st.pop();
                int x1=st.top();
                st.pop();
                int ans;
                if(x=="+"){
                    ans=x1+x2;
                }else if(x=="-"){
                    ans=x1-x2;
                }else if(x=="*"){
                    ans=x1*x2;
                }else{
                    ans=x1/x2;
                }
                st.push(ans);
            }else{
                st.push(stoi(x));
            }
        }
        return st.top();
    }
};
