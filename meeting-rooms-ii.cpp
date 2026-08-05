/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        int rooms = 0;
        int cnt = 0;
        vector<pair<int, int>> sweep;
        for(int i = 0; i < intervals.size(); i++){
            sweep.push_back({intervals[i].start, 1});
            sweep.push_back({intervals[i].end, -1});
        }
        sort(sweep.begin(), sweep.end());
        for(const auto& s: sweep){
            cnt+=s.second;
            rooms = max(rooms, cnt);
        }
        return rooms;
    }
};
