class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> pre(numCourses); // [[1]]
        vector<int> indeg(numCourses, 0); // [0 ,1]
        queue<int> take;
        int finished = 0;

        for(vector<int> prerequisite: prerequisites){
            pre[prerequisite[1]].push_back(prerequisite[0]);
            indeg[prerequisite[0]] = indeg[prerequisite[0]] + 1;
        } // pre = [[1]], indeg[0, 1]

        for(int i = 0; i < numCourses; i++){
            if(indeg[i] == 0){
                take.push(i);
            }
        } // take = [0]

        while(!take.empty()){
            int course = take.front(); // course = 0
            take.pop();
            finished++;
            for(int nex: pre[course]){ // [1]
                indeg[nex]--; // indeg = [0, 0]
                if(indeg[nex] == 0){
                    take.push(nex); // take = [1]
                }
            }
        }
        return (finished == numCourses);
    }
};