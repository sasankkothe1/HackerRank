/**
 * Created by sasank on 11.05.18.
 */
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Kangaroop {

    static String kangaroo(int x1, int v1, int x2, int v2) {
        if(v2>v1 && x2>x1 || v1>v2 && x1>x2)
        {
            return "NO";
        }
        for (int i = 0;  ; i++) {
            if(x1+(i*v1)==x2+(i*v2)){
                return "YES";
            }

        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int x1 = in.nextInt();
        int v1 = in.nextInt();
        int x2 = in.nextInt();
        int v2 = in.nextInt();
        String result = kangaroo(x1, v1, x2, v2);
        System.out.println(result);
    }
}