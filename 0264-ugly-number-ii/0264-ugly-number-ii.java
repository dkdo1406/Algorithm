class Solution {
    public int nthUglyNumber(int n) {
        // dp
        int[] primes = {2,3,5}; //ugly 조건
        int[] indices = {0,0,0}; // 곱을 몇번 사용했는지 체크
        List<Integer> uglyArr = new ArrayList<>(); // ugly 최소값
        uglyArr.add(1);

        for (int idx = 1; idx < n; idx++) {
            // 다음으로 올 수 있는 ugly 값 찾기
            int[] nextUglies = {
                uglyArr.get(indices[0]) * primes[0],
                uglyArr.get(indices[1]) * primes[1],
                uglyArr.get(indices[2]) * primes[2]
            };
            int minValue = Math.min(nextUglies[0], Math.min(nextUglies[1], nextUglies[2]));
            uglyArr.add(minValue);
            for (int i = 0; i < 3; i++) {
                if (minValue == nextUglies[i]) indices[i]++;
            }
        }

        return uglyArr.get(n-1);
    }
}