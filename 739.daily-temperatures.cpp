class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        stack<int> warmer;
        vector<int> answer(n, 0);

        for(int i = 0; i < n; i++){
            while(!warmer.empty() && temperatures[i] > temperatures[warmer.top()]){
                int top = warmer.top();
                answer[top] = i - top;
                warmer.pop();
            } 
            warmer.push(i);
        }
        return answer;
    }
};
