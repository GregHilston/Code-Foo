public class Solution  {
    /**
     * Determines if we can plant a flower at a given location in a specific flowerbed.
     * @param flowerBed state of flowerbed
     * @param i location to check
     * @return whether we can plant a flower or not
     */
    private boolean canPlantHere(int[] flowerBed, int i) {
        // left check
        int leftNeighborIndex = i - 1;

        if(leftNeighborIndex > 0) // ensures we don't go off the flower bed
        {
            if(flowerBed[leftNeighborIndex] == 1) {
                return false; // Can't plant next to a flower
            }
        }

        // right check
        int rightNeighborIndex = i + 1;

        if(rightNeighborIndex < flowerBed.length) // ensures we don't go off the flower bed
        {
            if(flowerBed[rightNeighborIndex] == 1) {
                return false; // Can't plant next to a flower
            }
        }

        return true;
    }

    /**
     * Determines if we can plant n new flowers in a specific flowerbed.
     * @param flowerBed initial state of flowerbed
     * @param n how many flowers we wish to plant
     * @return whether we can plant n new flowers in flowerBed
     */
    public boolean solve(int[] flowerBed, int n) {
        int planted = 0;

        for(int i = 0; i < flowerBed.length; i++) {
            if(planted == n) {
                return true;
            }

            if(flowerBed[i] == 0 && this.canPlantHere(flowerBed, i)) {
                flowerBed[i] = 1;
                planted += 1;
            }
        }

        return false;
    }
 }