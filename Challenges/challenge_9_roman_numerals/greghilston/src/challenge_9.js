"use strict" // forcing ourselves to write better NodeJS

const expectedNumberOfArguments = 3 // first for invoked node path, second for script path, third for multiline string 
let mappings = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

/**
 * Converts a string roman numeral value to an int value
 * 
 * @param {string} romanNumeralWritten 
 */
function convertRomanNumerals(romanNumeralWritten){
    let runningSum = 0

    for(var i = 0; i < romanNumeralWritten.length; i++) {
        if(!(romanNumeralWritten[i] in mappings)) {
            return undefined // an unexpected character was found
        }

        if((i == romanNumeralWritten.length - 1) || (mappings[romanNumeralWritten[i]] >= mappings[romanNumeralWritten[i + 1]])) {
            runningSum += mappings[romanNumeralWritten[i]]
        } else {
            runningSum -= mappings[romanNumeralWritten[i]]
        }
    }

    return runningSum
}

/**
 * main - Parsing command line arguments and calls our coding challenge method
 */
function main() {
    if (process.argv.length != expectedNumberOfArguments) {
        throw new Error("Unexpected number of input arguments. Expected " + expectedNumberOfArguments + " actual " + process.argv.length)
    }
    
    let romanNumeralWritten = process.argv[2]
    let integerValue = convertRomanNumerals(romanNumeralWritten)
}

// only call if main module and not being imported
if (!module.parent) {
    main()
}

module.exports = convertRomanNumerals // so our tests can access this method