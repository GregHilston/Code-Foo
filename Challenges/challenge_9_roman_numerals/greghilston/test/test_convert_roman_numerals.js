var chai = require('chai')
const convertRomanNumerals = require('../src/challenge_9')
const expect = chai.expect

describe('convertRomanNumerals', function() {
    it("'Valid Input (1 Through 100)", function() {
        // given
        validInputAndOutput = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
                          "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19, "XX": 20,
                          "XXI": 21, "XXII": 22, "XXIII": 23, "XXIV": 24, "XXV": 25, "XXVI": 26, "XXVII": 27, "XXVIII": 28, "XXIX": 29, "XXX": 30}

        // when
        for (let input in validInputAndOutput) {
            const returnedValue = convertRomanNumerals(input) 

            // then
            expect(validInputAndOutput[input]).to.equal(returnedValue)
        }
    })

    it("'Invalid Input Handled Appropriately", function() {
        // given
        validInputAndOutput = {"ABC": undefined, "XLXX": undefined}

        // when
        for (let input in validInputAndOutput) {
            const returnedValue = convertRomanNumerals(input) 

            // then
            expect(validInputAndOutput[input]).to.equal(returnedValue)
        }
    })
})