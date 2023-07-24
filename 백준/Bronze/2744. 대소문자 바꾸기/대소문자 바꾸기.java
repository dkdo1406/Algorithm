import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt")); 
		
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		char[] cArr = new char[s.length()];
		for(int idx = 0; idx < s.length(); idx++) {
			if( s.charAt(idx) >= 'a') {
				cArr[idx] = (char) ((s.charAt(idx) - 32));
			} else {
				cArr[idx] = (char) ((s.charAt(idx) + 32));
			}
		}
		String ans = new String(cArr);
		System.out.println(ans);
		
	}

}
