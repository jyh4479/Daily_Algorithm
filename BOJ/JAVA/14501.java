import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static Integer ans = Integer.MIN_VALUE;

	public static void checkCanWork(Integer[] dayList, Integer[] payList, boolean[] checkList, Integer cnt) {
		if (cnt >= checkList.length) {
			Integer workSum = 0;
			for (int i = 0; i < checkList.length; i++) {
				if (checkList[i]) workSum += payList[i];
			}
			ans = Math.max(ans, workSum);

//            System.out.print(Arrays.toString(checkList));
//            System.out.println(workSum);

			return;
		}

		for (int i = cnt; i < checkList.length; i++) {
			if (!checkList[i]) {
				if (i + dayList[i] <= checkList.length) checkList[i] = true;
				checkCanWork(dayList, payList, checkList, i + dayList[i]);
				checkList[i] = false;
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		Integer[] dayList = new Integer[N];
		Integer[] payList = new Integer[N];
		boolean[] checkList = new boolean[N];

		for (int i = 0; i < N; i++) {
			int day = sc.nextInt();
			int pay = sc.nextInt();

			dayList[i] = day;
			payList[i] = pay;
			checkList[i] = false;
		}

		checkCanWork(dayList, payList, checkList, 0);
		System.out.println(ans);
	}
}
