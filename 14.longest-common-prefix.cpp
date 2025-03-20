class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty()) return "";
        string ans = strs[0];
        
        for(int i=1; i<strs.size(); i++){
            int j = 0;
            while(j<ans.size() && j<strs[i].size() && strs[i][j]==ans[j]){
                j++;
            }
            ans = ans.substr(0, j);
            if(ans=="") return ans;
        }
        return ans;
    }
};
