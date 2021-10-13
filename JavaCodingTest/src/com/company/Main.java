package com.company;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("HelloWorld!");

        for (int i = 0; i < 5; i++) {
            System.out.println(i+" hello");
        }
        
        Queue<Integer> q = new LinkedList<>();
        Stack<Integer> s = new Stack<>();
        Deque<Integer> d = new LinkedList<>();

        for(int i=0;i<9;i++){
            q.add(i);
            s.add(i);
        }

        while(!q.isEmpty()){
            System.out.println(q.poll());
        }
        System.out.println(q);

        while(!s.empty()){
            System.out.println(s.pop());
        }
        System.out.println(s);
    }
}
