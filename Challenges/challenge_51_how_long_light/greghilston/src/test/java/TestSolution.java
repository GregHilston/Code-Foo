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
        int result = solution.solve("1 3\n2 3\n4 5");
        assertEquals(3, result);
    }

    @Test
    public void testTwo()  {
        int result = solution.solve("2 4\n3 6\n1 3\n6 8");

        assertEquals(7, result);
    }

    @Test
    public void testThree()  {
        int result = solution.solve("6 8\n5 8\n8 9\n5 7\n4 7");

        assertEquals(5, result);
    }
}
