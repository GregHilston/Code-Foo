module Main where
import Test.HUnit

testSum = TestCase $ assertEqual "10 + 5 = 15" 15 (10 + 5)

testProd = TestCase $ assertEqual "10 * 15" 150 (10 * 15)

testPred = TestCase $ assertBool "10 > 5" (10 > 5)

testFailure = TestCase $ assertEqual "It will fail 10 + 2 = 15" (10 + 2) 15  

testlist = TestList [TestLabel "testSum" testSum,
                    TestLabel "testPred" testPred,
                    TestLabel "testFailure" testFailure,
                    TestLabel "testProd" testProd                    
                    ]

main :: IO ()
main = do
  runTestTT testlist
  return ()
