import java.util.ArrayList;

public class CafeUtil {
    public int getStreakGoal(int numWeeks) {
        int total = 0;
        for(int i = 0; i < numWeeks; i++) {
            total += i + 1;
        }

        return total;
    }

    public double getOrderTotal(double[] prices) {
        double doubleTotal = 0.00;
        for(double price: prices) {
            doubleTotal += price;
        }
        return doubleTotal;
    }

    public void displayMenu(ArrayList<String> menuItems) {
        for(String coffeeName: menuItems) {
            System.out.println(coffeeName);
        }
    }

    public void addCustomer(ArrayList<String> customers) {
        System.out.println("Please enter your name:");
        String userName = System.console().readLine();
        System.out.println("Hello, " + userName);
        System.out.println("There are " + customers.size() + " people in front of you");
        customers.add(userName);
        for(String name: customers) {
            System.out.println(name);
        }
    }

    public void printPriceChart(String product, double price, int maxQuantity) {
        System.out.println(product);
        for(int k = 0; k < maxQuantity; k++) {
            System.out.println((k+1) + " - $" + (price * (k+1)));
        }
    }

    public boolean displayMenu(ArrayList<String> menuItems, ArrayList<Double> prices) {
        if(menuItems.size() != prices.size()) {
            return false;
        } else {
            for(int l = 0; l < menuItems.size(); l++) {
                System.out.println(l + " " + menuItems.get(l) + " -- $" + prices.get(l));
            }
            return true;
        }
    }

    public String[] addCustomers() {
        ArrayList<String> customerNames = new ArrayList<String>();
        int keepAdding = 1;
        while(keepAdding == 1){
            System.out.println("Testing");
            String customerName = System.console().readLine();
            if (customerName.equals("q")) {
                keepAdding -= 1;
            } else {
                customerNames.add(customerName);
            }
        }
        String[] customers = new String[customerNames.size()];
        for(int m = 0; m < customerNames.size(); m++) {
            customers[m] = customerNames.get(m);
        }
        return customers;
    }
}