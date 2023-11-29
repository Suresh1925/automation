package automation.Suresh_Task;

import java.time.Year;

public class ListOfLeapYears {
    public static void main(String[] args) 
    {
        System.out.println(args[0].getClass());
            int first =Integer.parseInt(args[0]);
            int last=Integer.parseInt(args[1]);
            for (int year = first; year <= last; year++)
            {
                if (Year.of(year).isLeap()) 
                {
                    System.out.println(year);
                }
            }
        }
    }