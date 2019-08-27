/* Progress tax challenge
 income cap      marginal tax rate
   10,000           0.00 (0%)
   30,000           0.10 (10%)
  100,000           0.25 (25%)
    ++              0.40 (40%)
*/
import Foundation

func tax(on income: Int) -> Int {
    var remaining = income
    var tax = 0
    let rates = [(10000, 0), (20000, 10), (70000, 25)]

    for (range, rate) in rates {
        guard remaining > range else {
            return tax + remaining * rate / 100
        }
        tax += range * rate / 100
        remaining -= range
    }

    return tax + remaining * 40 / 100
}

let startTime = CFAbsoluteTimeGetCurrent()
print("Tax on $0 is calculated to be $\(tax(on: 0)) (should be: $0)")
print("Tax on $10000 is calculated to be $\(tax(on: 10000)) (should be: $0)")
print("Tax on $10009 is calculated to be $\(tax(on: 10009)) (should be: $0)")
print("Tax on $10010 is calculated to be $\(tax(on: 10010)) (should be: $1)")
print("Tax on $12000 is calculated to be $\(tax(on: 12000)) (should be: $200)")
print("Tax on $56789 is calculated to be $\(tax(on: 56789)) (should be: $8697)")
print("Tax on $1234567 is calculated to be $\(tax(on: 1234567)) (should be: $473326)")
print("Tax on $100000000 is calculated to be $\(tax(on: 100000000))")
print("It took \(CFAbsoluteTimeGetCurrent() - startTime) seconds to calculate.")
