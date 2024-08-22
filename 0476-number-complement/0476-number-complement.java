class Solution {
    public int findComplement(int num) {
        // 10 -> 2
        String binary = Integer.toBinaryString(num);
        // 2 -> XOR
        String opposite = "1".repeat(binary.length());
        int xor = Integer.parseInt(opposite,2);
        return num ^ xor;
    }
}