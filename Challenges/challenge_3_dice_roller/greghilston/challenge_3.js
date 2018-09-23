"use strict" // forcing ourselves to write better Nodejs

const seedrandom = require('seedrandom');
const assert = require('assert')

const rand = seedrandom('1337') // seeding so we have deterministic results for testing

// from: https://stackoverflow.com/a/7228322/1983957
function randomIntFromInterval(min, max) {
    return Math.floor(rand() * (max - min + 1) + min);
}

function roll(input) {
    const split = input.split('d')
    const numberOfDie = parseInt(split[0], 10) // referred to as numberOfDie in our challenge
    const sidesOfDie = parseInt(split[1], 10) // referred to as sidesOfDie in our challenge

    // input validation
    if (isNaN(numberOfDie) || isNaN(sidesOfDie)) {
        return ""
    }

    // range checking on input
    if ((numberOfDie < 1 || numberOfDie > 100) || (sidesOfDie < 2 || sidesOfDie > 100)) {
        return ""
    }

    let sum = 0
    let rolls = []

    for (let i = 0; i < numberOfDie; i++) {
        const roll = randomIntFromInterval(1, sidesOfDie)
        rolls.push(roll)
        sum += roll
    }

    console.log(sum + ": " + rolls.join(" "))

    return sum
}

// example tests from challenge
assert.equal("", roll("0d100"), "numberOfDie is not in range [1-100] range, therefore empty string is expected")
assert.equal("", roll("1d1"), "sidesOfDie is not in range [2-100] range, therefore empty string is expected")
assert.equal("", roll("1d101"), "sidesOfDie is not in range [2-100] range, therefore empty string is expected")
assert.equal("", roll("101d2"), "numberOfDie is not in range [1-100] range, therefore empty string is expected")

const five_d_twelve = roll("5d12")
assert(five_d_twelve >= 5, "some number between 5 and 60, probably closer to 32 or 33")
assert(five_d_twelve <= 60, "some number between 5 and 60, probably closer to 32 or 33")
assert(five_d_twelve == 36, "Should exactly match, as using same seed")

const six_d_four = roll("6d4")
assert(six_d_four >= 6, "some number between 6 and 24, probably around 15")
assert(six_d_four <= 24, "some number between 6 and 24, probably around 15")
assert(six_d_four == 14, "Should exactly match, as using same seed")

const one_d_eight = roll("1d8")
assert(one_d_eight >= 1, "some number between 1 and 8")
assert(one_d_eight <= 8, "some number between 1 and 8")
assert(one_d_eight == 7, "Should exactly match, as using same seed")

const three_d_six = roll("3d6")
assert(three_d_six >= 3, "some number between 3 and 18, probably around 9")
assert(three_d_six <= 18, "some number between 3 and 18, probably around 9")
assert(three_d_six == 12, "Should exactly match, as using same seed")

const four_d_twenty = roll("4d20")
assert(four_d_twenty >= 4, "some number between 4 and 80, probably around 40")
assert(four_d_twenty <= 80, "some number between 4 and 80, probably around 40")
assert(four_d_twenty == 41, "Should exactly match, as using same seed")

const one_hundred_d_one_hundred = roll("100d100")
assert(one_hundred_d_one_hundred >= 100, "some number between 100 and 10000, probably around 5000")
assert(one_hundred_d_one_hundred <= 10000, "some number between 100 and 10000, probably around 5000")
assert(one_hundred_d_one_hundred == 4853, "Should exactly match, as using same seed")

// additional tests checking bad input
assert.equal("", roll(""), "No input should fail input validation and return an empty string")
assert.equal("", roll(""), "Bad input should fail input validation and return an empty string")
assert.equal("", roll("adb"), "Bad input should fail input validation and return an empty string")
assert.equal("", roll("3.14d1.59"), "Bad input should fail input validation and return an empty string")
