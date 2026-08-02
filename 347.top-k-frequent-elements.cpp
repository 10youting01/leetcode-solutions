class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        vector<int> topk;

        for(int x: nums){
            if(freq.find(x) == freq.end()){
                freq[x] = 1;
            } else{
                freq[x] = freq[x] + 1;
            }
        }

        for(const auto& [num, cnt]: freq){
            if(minHeap.size() >= k){
                const auto& [cnt_top, num_top] = minHeap.top();
                if(cnt > cnt_top){
                    minHeap.pop();
                    minHeap.push({cnt, num});
                } 
            } else{
                minHeap.push({cnt, num});
            }
        }

        while(!minHeap.empty()){
            const auto& [cnt, num] = minHeap.top();
            topk.push_back(num);
            minHeap.pop();
        }
        return topk;
    }
};