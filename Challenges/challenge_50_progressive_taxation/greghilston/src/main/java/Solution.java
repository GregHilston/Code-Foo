import java.util.*;

public class Solution  {
    /**
     * Calculates tax rate for Examplania.
     *
     * This is probably my worst solution to and Code Foo. Ever.
     *
     * @param income to evaluate
     * @return tax rate
     */
    public int solve(int income) {
        int taxRate = 0;
        // Ordered list of maximum value to tax rate for all but last bucket
        Map<Integer, Double> allButLastBucketTaxRates = new LinkedHashMap<>() {{
                put(10000, 0.0);
                put(20000, 0.10);
                put(70000, 0.25);
        }};

        // Ordered list of maximum value to tax rate for all but last bucket
        Map<Integer, Integer> allButLastBucketUsed = new LinkedHashMap<>() {{
            put(10000, 0);
            put(20000, 0);
            put(70000, 0);
        }};


        int remainingIncome = income;
        for (int key : allButLastBucketTaxRates.keySet()) {
            Double value = allButLastBucketTaxRates.get(key);
            System.out.println("\nremainingIncome: " + remainingIncome);
            System.out.println("taxRate: " + taxRate);
            System.out.println("key: " + key);
            System.out.println("value: " + value);

            int remainingBucket = key - remainingIncome; // negative number repsents more income to be taxed
            System.out.println("remainingBucket: " + remainingBucket);
            // check if remaining bucket is entirely used
            if (remainingBucket < 0) {
                System.out.println("\tsetting remainingBucket to 0");
                remainingBucket = 0; // no negative remainingBucket
            }

            remainingIncome = remainingIncome - key; // negative number represents more in this bucket remains
            System.out.println("remainingIncome: " + remainingIncome);

            // check if used entire income
            if (remainingIncome < 0) {
                System.out.println("\tsetting remainingIncome to 0");
                remainingIncome = 0;
            }

            int howMuchBucketUsed = key - remainingBucket;
            System.out.println("howMuchBucketUsed: " + howMuchBucketUsed);
            // check if used entire bucket
            if (howMuchBucketUsed > key) {
                System.out.println("\tsetting howMuchBucketUsed to 0");
                howMuchBucketUsed = key;
            }

            int addToTaxRate = (int) Math.floor(howMuchBucketUsed * value);
            System.out.println("howMuchBucketUsed * value: " + howMuchBucketUsed * value);
            System.out.println("addToTaxRate: " + addToTaxRate);
            taxRate += addToTaxRate;
            income -= howMuchBucketUsed;

            if (remainingIncome == 0) {
                System.out.println("returning taxRate: " + taxRate);
                return taxRate;
            }
        }

        System.out.println("\noverflow bucket");
        System.out.println("remainingIncome: " + remainingIncome);
        if (remainingIncome > 0) {
            taxRate += remainingIncome * 0.4;
            System.out.println("adding: " + remainingIncome * 0.4);

        }

        System.out.println("returning taxRate: " + taxRate);
        return taxRate;
    }

    public static void main (String[] args) {
        new Solution().solve(0);
    }
 }