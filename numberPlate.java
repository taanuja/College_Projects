import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class numberPlate {

    public static boolean isValidNumberPlate(String plate) {

        String regex = "^[A-Z]{2}\\s\\d{2}\\s[A-Z]{2}\\s\\d{4}$";

        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(plate);

        return matcher.matches();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the vehicle number plate (format: XX NN YY NNNN): ");
        String numberPlate = scanner.nextLine();

        if (isValidNumberPlate(numberPlate)) {
            System.out.println(numberPlate + " is a valid number plate.");
        } else {
            System.out.println(numberPlate + " is NOT a valid number plate.");
        }

        scanner.close();
    }
}
