package automation.Suresh_Task;

import java.time.Year;

public class ListOfLeapYears {
    public static void main(int[] args) {
            int first =args[0];
            int last=args[1];
            for (int year = first; year <= last; year++)
            {
                if (Year.of(year).isLeap()) 
                {
                    System.out.println(year);
                }
            }
        }
    }