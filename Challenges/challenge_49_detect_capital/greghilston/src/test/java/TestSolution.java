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
        boolean result = solution.solve("USA");

        assertTrue("All capitals.", result);
    }

    @Test
    public void testTwo()  {
        boolean result = solution.solve("FlaG");

        assertFalse("Lowercase a grouped with the rest of capitals.", result);
    }
}
