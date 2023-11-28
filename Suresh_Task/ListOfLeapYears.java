package automation.Suresh_Task;

public class ListOfLeapYears {
    public static void main(String[] args) {
    for (int i = 1800; i < 1900; i++) {
        if ((i % 4 == 0 && i % 100 != 0) || i % 400 == 0) {
            System.out.printf("%4d%n", i);
        }
    }
}
}