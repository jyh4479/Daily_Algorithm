package com.company.practice;

import java.util.ArrayList;

public class Array {
    public static void main(String[] arg) {
        ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i < 5; i++) {
            graph.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                graph.get(i).add(0);
            }
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(graph.get(i).get(j));
            }
            System.out.println();
        }
//        Scanner sc = new Scanner(System.in);
//        int a = sc.nextInt();
//        int b = sc.nextInt();
//        int c = sc.nextInt();
//        int d = sc.nextInt();
//
//        System.out.print(a);
//        System.out.println(b);
//        System.out.println(c);
//        System.out.println(d);
    }
}
