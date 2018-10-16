var chai = require('chai')
const convertRomanNumerals = require('../src/challenge_9')

describe('convertRomanNumerals', function() {
    it("'1 Through 100", function() {
        // given
        inputAndOutput = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
                          "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19, "XX": 20,
                          "XXI": 21, "XXII": 22, "XXIII": 23, "XXIV": 24, "XXV": 25, "XXVI": 26, "XXVII": 27, "XXVIII": 28, "XXIX": 29, "XXX": 30}
        let returnedValue

        // when
        for (var input in inputAndOutput) {
            returnedValue = convertRomanNumerals(input) 

            // then
            chai.assert.isTrue(inputAndOutput[input] == returnedValue, "should be correct value")
        }
    })
})