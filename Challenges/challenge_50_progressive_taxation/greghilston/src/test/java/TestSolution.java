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
        int result = solution.solve(0);

        assertEquals(0, result);
    }

    @Test
    public void testTwo()  {
        int result = solution.solve(10000);

        assertEquals(0, result);
    }

    @Test
    public void testThree()  {
        int result = solution.solve(10009);

        assertEquals(0, result);
    }

    @Test
    public void testFour()  {
        int result = solution.solve(10010);

        System.out.println("result " + result);

        assertEquals(1, result);
    }

    @Test
    public void testFive()  {
        int result = solution.solve(12000);

        assertEquals(200, result);
    }

    @Test
    public void testSix()  {
        int result = solution.solve(56789); // 10000 * 0.0 + 30000 * 0.10 + 16789 * .25

        assertEquals(8697, result);
    }

    @Test
    public void testSeven()  {
        int result = solution.solve(1234567);

        assertEquals(473326, result);
    }

    // I made this test
    @Test
    public void testEight()  {
        int result = solution.solve(140010); // 10000 * 0.0 + 30000 * 0.10 + 100000 * 0.25 + 10 * 0.40

        assertEquals(28004, result);
    }
}
