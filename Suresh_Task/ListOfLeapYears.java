package automation.Suresh_Task;

import java.time.Year;
import java.util.Scanner;

public class ListOfLeapYears {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the first year: ");
            int first = scanner.nextInt();

            System.out.print("Enter the last year: ");
            int last = scanner.nextInt();

            System.out.println("Leap years between 1992 and 2010:");
            for (int year = first; year <= last; year++) {
                if (Year.of(year).isLeap()) {
                    System.out.println(year);
                }
            }
        }
    }
}