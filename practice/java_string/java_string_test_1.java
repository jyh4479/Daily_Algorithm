import java.util.*;

public class main {
	public static void main(String[] args) {
		StringBuilder a = new StringBuilder("dsadasd asdasd");

		for(int i=0;i<a.length();i++) {
			if(a.charAt(i)=='a') {
				a.setCharAt(i, 'x');
			}
		}
		System.out.println(a);
	}
}