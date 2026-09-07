class Solution {
public:
    string reverseParentheses(string s) {
        stack<char> st;
        for(int i=0;i<s.length();i++){
            while(i<s.length() && s[i] != ')'){
                st.push(s[i]);
                i++;
            }
            string tmp="";
            if(s[i] == ')'){
                while(!st.empty() && st.top() != '('){
                    tmp+=st.top();
                    st.pop();
                }
                st.pop();
                for(auto x:tmp){
                    st.push(x);
                }
            }
        }
        s="";
        while(!st.empty()){
            s += st.top();
            st.pop();
        }
        reverse(s.begin(),s.end());
        return s;
    }
};