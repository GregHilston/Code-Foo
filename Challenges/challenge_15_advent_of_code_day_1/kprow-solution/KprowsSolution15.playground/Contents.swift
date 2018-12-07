import UIKit

if let inputFile = Bundle.main.url(forResource: "input", withExtension: "txt") {
    let inputFileContents = try String(contentsOf: inputFile, encoding: .utf8)
    let inputs = inputFileContents.split(separator: "\n")
    var total = 0
    for input in inputs {
        total += Int(input) ?? 0
    }
    print(total)
}
