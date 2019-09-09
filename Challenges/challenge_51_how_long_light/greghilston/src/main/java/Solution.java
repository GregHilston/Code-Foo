import java.util.Set;
import java.util.HashSet;

public class Solution {
    public int solve(String input) {
        Set<Integer> timeIntervals = new HashSet<Integer>();
        int minStartTime = Integer.MAX_VALUE;
        int maxEndTime = Integer.MIN_VALUE;
        int timeIntervalsLit = 0;

        String[] tokens = input.split("\n");

        for (String token : tokens) {
            int startTime = Integer.parseInt(token.split(" ")[0]);
            int endTime = Integer.parseInt(token.split(" ")[1]);

            for (int i = startTime; i < endTime; i++) {
                timeIntervals.add(i);
            }

            if (startTime < minStartTime) {
                minStartTime = startTime;
            }

            if (endTime > maxEndTime) {
                maxEndTime = endTime;
            }
        }

        for (int i = minStartTime; i <= maxEndTime; i++) {
            if (timeIntervals.contains(i)) {
                timeIntervalsLit += 1;
            }
        }

        return timeIntervalsLit;
    }
}