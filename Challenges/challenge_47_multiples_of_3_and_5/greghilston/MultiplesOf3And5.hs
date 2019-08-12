ifNDivisibleByM :: (Integer, Integer) -> Bool
ifNDivisibleByM (n, m) = if n `rem` m == 0 then True else False

euler_1 :: Integer -> Integer
euler_1 0 = 0
euler_1 n = if ifNDivisibleByM(n, 3) then n+euler_1(n-1) else if ifNDivisibleByM(n, 5) then n+euler_1(n-1) else euler_1(n-1)

main = do 
   putStrLn "The sum of first thousand natural numbers divisible by three or five:"  
   print(euler_1(999))