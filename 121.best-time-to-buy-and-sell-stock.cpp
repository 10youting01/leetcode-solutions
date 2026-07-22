class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int curr_min = 10000;
        int max_profit = 0;

        for(int i = 0; i < prices.size(); i++){
            if(prices[i] < curr_min){
                curr_min = prices[i];
            } if((prices[i] - curr_min) > max_profit){
                max_profit = prices[i] - curr_min;
            }
        }
        return max_profit;
    }
};


// 這一題的輸入是一個 array，每一個數字代表股票在該天的價格。輸出則是在哪一天買以及在哪一天賣可以賺最多的錢；如果沒有辦法賺錢的話，就回傳 0，代表不要買股票。

// 限制的部分：
// 1. array 的長度大概是從 1 到 10 的 5 次方
// 2. 每個股票的價格（每一個值）在 0 到 10 的 4 次方之間

// 如果是暴力解的話，就以每一天都當作買股票的日期，然後往後去找哪一天賣可以讓這一天買賺最多錢。每一個位置都這樣做一次，再去比較哪一個值最大，然後回傳。像這樣的暴力解，時間複雜度大約是 Big O(n^2)，因為每個值都要往後找一次。

// 比較好的解法，應該會是走訪這個 array，然後同時維護兩個變數，也就是 current_min 跟 max_profit。

// 如果目前走到的位置的值比 current_min 小，那 current_min 就更新；如果目前位置的值減掉 current_min 大於 max_profit 的話，就更新 max_profit 的值。

// 最後回傳 max_profit。
