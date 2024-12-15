class Solution {
    public long continuousSubarrays(int[] nums) {
        int N = nums.length;
        long ans = 0;
        // 서브쿼리가 만족하는 기준
        // 1개는 모두 만족

        // 첫번째 값을 기준으로 뒤에것을 계속 비교한다.
        int l = 0;
        int r = 0;
        int[] rank = new int[5];
        for (int idx = 0; idx < 5; idx++) {
            rank[idx] = -1;
        }
        rank[2] = 0;
        int maxIdx = 0;
        int minIdx = 0;

        // 계산방법
        // l에서 현재위치 전까지 계산.
        // 그다음 l위치까지 계산결과 빼기
        // 반복
        while (l < N && r < N) {
            // 성립이 안되는 경우
            if (Math.abs(nums[maxIdx] - nums[r]) > 2 || Math.abs(nums[minIdx] - nums[r]) > 2) {
                ans += (long)(1 + r - l) * (r - l) / 2;
                
                // max나 min중 성립이 안되는 마지막 idx의 다음 idx로 l을 이동시킨다.
                // 최대값이 문제인 경우
                if (Math.abs(nums[maxIdx] - nums[r]) > 2 && Math.abs(nums[minIdx] - nums[r]) > 2) {
                    // 계산을 더 할 필요없이 바로 l을 r로 이동
                    l = r;
                    for (int idx = 0; idx < 5; idx++) {
                        rank[idx] = -1;
                    }
                    rank[2] = l;
                    
                } else {
                    if (Math.abs(nums[maxIdx] - nums[r]) > 2) {
                        l = maxIdx + 1;
                        if (nums[l] == nums[maxIdx]) {
                            for (int idx = 0; idx < 5; idx++) {
                                if (rank[idx] < l || nums[rank[idx]] == nums[maxIdx]) continue;
                                l = Math.min(l, rank[idx]);
                            }
                        }
                        rank = sort(l, r, nums, rank);
                    }
                    // 최소값이 문제인 경우
                    else {
                        l = minIdx + 1;
                        
                        if (nums[l] == nums[minIdx]) {
                            for (int idx = 0; idx < 5; idx++) {
                                if (rank[idx] < l || nums[rank[idx]] == nums[minIdx]) continue;
                                l = Math.min(l, rank[idx]);
                            }
                        }
                        rank = sort(l, r, nums, rank);

                    }
                    ans -= (long)(1 + r - l) * (r - l) / 2;
                    int[] val = findVal(l, rank, nums);
                    maxIdx = val[0];
                    minIdx = val[1];

                }
                if (nums[r] >= nums[maxIdx]) {
                    maxIdx = r;
                }
                if (nums[r] <= nums[minIdx]) {
                    minIdx = r;
                }
                
            }
            else {
                if (nums[l] <= nums[r]) {
                    rank[2 + nums[r] - nums[l]] = r;
                } else {
                    rank[2 - (nums[l] - nums[r])] = r;
                }
                if (nums[r] >= nums[maxIdx]) {
                    maxIdx = r;
                }
                if (nums[r] <= nums[minIdx]) {
                    minIdx = r;
                }
                r += 1;
            }
            if (r == N) {
                ans += (long)(1 + r - l) * (r - l) / 2;
                break;
            }
        }
        return ans;
    }
    // 재정렬
    public int[] sort(int l, int r, int[] nums, int[] rank) {
        int curr = nums[l];
        int past = nums[rank[2]];
        // r이 이동한거라면
        if (curr == past) {
            if (nums[l] <= nums[r]) {
                rank[2 + nums[r] - nums[l]] = Math.max(l, r);
            } else {
                rank[2 - (nums[l] - nums[r])] = Math.max(l, r);
            }
        } else {
            // 두 값의 차이를 찾는다.
            int diff = Math.abs(past - curr);
            for (int idx = 0; idx < 5; idx++) {
                if (rank[idx] < l) rank[idx] = -1;
            }
            if (past < curr) {
                for (int idx = 0; idx < 5; idx++) {
                    if (idx + diff > 4) {
                        rank[idx] = -1;
                    } else {
                        rank[idx] = rank[idx + diff];
                    }
                    
                }
            } else {
                for (int idx = 0; idx < 5; idx++) {
                    if (4 - (idx + diff) < 0) {
                        rank[4 - idx] = -1;
                    } else {
                        rank[4 - idx] = rank[4 - (idx + diff)];
                    }
                }
            }
        }

        

        return rank;

    }

    public int[] findVal(int index, int[] rank, int[] nums) {
        int maxVal = nums[rank[2]];
        int minVal = nums[rank[2]];
        int[] val = new int[2];
        val[0] = index;
        val[1] = index;
        for (int idx = 0; idx < 5; idx++) {
            if (rank[idx] == -1 || rank[idx] < index) continue;
            if (maxVal <= nums[rank[idx]]) {
                maxVal = nums[rank[idx]];
                val[0] = rank[idx];
            }
            if (minVal >= nums[rank[idx]]) {
                minVal = nums[rank[idx]];
                val[1] = rank[idx];
            }
        }
        return val;
    }

}