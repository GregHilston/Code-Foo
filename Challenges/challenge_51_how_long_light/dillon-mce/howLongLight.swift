import Foundation

func howLongIsLightOn(in periods: String) -> Int {
    // Parse input
    let periods = periods.components(separatedBy: .newlines)
        .map { $0.components(separatedBy: .whitespaces).compactMap { Int($0) } }
    // Get the largest possible value
    let max = periods.flatMap { $0 }.max() ?? 0
    var possibleHours = Array(repeating: 0, count: max)

    // Mark the hours the light is on
    periods.forEach {
        for i in $0[0]..<$0[1] {
            possibleHours[i] = 1
        }
    }
    // Return the total
    return possibleHours.reduce(0, +)
}

let testData1 = """
1 3
2 3
4 5
"""

let testData2 = """
2 4
3 6
1 3
6 8
"""

let testData3 = """
6 8
5 8
8 9
5 7
4 7
"""

let testData4 = """
15 18
13 16
9 12
3 4
17 20
9 11
17 18
4 5
5 6
4 5
5 6
13 16
2 3
15 17
13 14
"""

let testDatas = [testData1, testData2, testData3, testData4]

let startTime = CFAbsoluteTimeGetCurrent()
for (index, testData) in testDatas.enumerated() {
    let answer = howLongIsLightOn(in: testData)
    print("The answer for the test data \(index + 1) is: \(answer)")
}
print("It took \(CFAbsoluteTimeGetCurrent() - startTime) seconds to find the answers")
