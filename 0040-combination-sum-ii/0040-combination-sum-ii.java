class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> res = new ArrayList();
        backTracking(0, candidates, target, res, new ArrayList<>());

        return res;
    }

    static void backTracking(int index, int[] arr, int target, List<List<Integer>> res, List<Integer> temp) {
        if(target == 0) {
            res.add(new ArrayList<>(temp));
            return;
        }

        for (int idx = index; idx < arr.length; idx++) {
            if (idx > index && arr[idx] == arr[idx - 1]) continue;
            if (arr[idx] > target) break;
            temp.add(arr[idx]);
            backTracking(idx + 1, arr, target - arr[idx], res, temp);
            temp.remove(temp.size() - 1);
        }
    }
}