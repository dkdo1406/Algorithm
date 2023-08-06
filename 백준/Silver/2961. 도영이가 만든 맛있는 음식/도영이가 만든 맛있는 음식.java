import java.util.*;
import java.io.*;

/*
 * 도영이가 만든 맛있는 음식
 *
 * 1. 신맛과 쓴맛을 입력 받고 재료들을 조합한다.
 * 2. 이 때, 신맛은 곱하고 쓴맛은 값을 더한다.
 * 3. 도영이는 쓴맛과 신맛의 차이가 작은 음식을 선호하므로 차이가 작은 값을 조합하여 출력한다.
 * 4. 단, 최소 1개는 선택해야 한다.
 * 
 * 
 * 구현
 * 쓴맛과 신맛의 차이인 변수 ans를 선언하고 최소값으로 값을 저장한다.
 * 쓴맛과 신맛이 있는 재료 배열을 만들어 저장한다.
 * 이 배열들을 조합하여 첫 인덱스부터 끝 인덱스까지 확인한다.
 * 확인하는 과정에서 쓴맛과 신맛의 차이가 ans보다 작으면 ans에 저장한다.
 * 
 * 
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;

	static int N, R, visit;
	static int ans = Integer.MAX_VALUE;
	static Ingredient[] ingredients;

	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt"));

		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine().trim(), " ");
		sb = new StringBuilder();
		
		N = Integer.parseInt(st.nextToken()); // 재료 수 
		
		ingredients = new Ingredient[N];

		int S, B;
		for(int idx = 0; idx < N; idx++) {
			st = new StringTokenizer(br.readLine().trim(), " ");
			S = Integer.parseInt(st.nextToken()); // 신 맛
			B = Integer.parseInt(st.nextToken()); // 쓴 맛
			ingredients[idx] = new Ingredient(S, B);
		}
		
		// 신맛은 곱이기 때문에 1을, 쓴맛은 합이기 때문에 0으로 초기값을 설정한다.

		cook(0, 1, 0);
		
		System.out.println(ans);

	}
	

	private static void cook(int depth, int sour, int bitter) {
		if (depth == N) return;

		for(int idx = depth; idx < N; idx++) {
			
			int res = Math.abs((ingredients[idx].sour * sour) - (ingredients[idx].bitter + bitter));
			ans = Math.min(ans, res);
			cook(idx + 1, ingredients[idx].sour * sour, ingredients[idx].bitter + bitter);
		}
	}

	
}

/**
 * 재료 클래스
 * 신맛과 쓴맛을 파라미터로 입력받는다.
 */
class Ingredient {
	int sour, bitter;
	public Ingredient(int sour, int bitter) {
		this.sour = sour;
		this.bitter = bitter;
	}
}

