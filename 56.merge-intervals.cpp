class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> merged;
        sort(intervals.begin(), intervals.end());

        for(const auto& interval: intervals){
            if(merged.empty()){
                merged.push_back(interval);
            } else{
                if(interval[0] <= merged.back()[1]){ // overlap
                    merged.back()[1] = max(interval[1], merged.back()[1]);
                } else{ // non overlap
                    merged.push_back(interval);
                }
            }
        }
        return merged;
    }
