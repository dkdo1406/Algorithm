import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine().trim());
        sb = new StringBuilder();
        
        int N =  Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine().trim());
        String S = st.nextToken();
        double r = 1;
        double M = 1234567891;
        double ans = S.charAt(0) - 96;
        
        for (int idx = 1; idx < N; idx++) {
            r *= 31;
            r %= M;
            ans += (S.charAt(idx)-96) * r;
        }
        System.out.println((int)(ans % M));
        


    }
}
