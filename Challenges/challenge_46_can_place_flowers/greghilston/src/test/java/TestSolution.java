import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.After;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class TestSolution {
    private Solution solution;

    @Before
    public void setUp() throws Exception {
        solution = new Solution();
    }

    @Test
    public void testOne()  {
        boolean result = solution.solve(new int[] {1,0,0,0,1}, 1);

        assertTrue("There should be room to plant one flower, dead center of the flower bed.", result);
    }

    @Test
    public void testTwo()  {
        boolean result = solution.solve(new int[] {1,0,0,0,1}, 2);

        assertFalse("There should not be room to plant two flowers. We only have room dead center.", result);
    }
}
