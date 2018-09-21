"use strict" // forcing ourselves to write better NodeJS

const fs = require("fs")
const parse = require('csv-parse/lib/sync')
const inputFile = "challenge_4_input.csv"
const assert = require('assert')

// column indexes
const nameColumn = 0
const birthDateColumn = 1
const birthPlaceColumn = 2 // not used
const deathDateColumn = 3
const deathPlaceColumn = 4 // not used

// object keys
const birthYearKey = "birthYear"
const deathYearKey = "deathYear"

/**
 * parseYear - Parses a year from a column from the input csv
 *
 * @param  {string} column - a column from the input csv
 * @returns {number}       - the number version of the column
 */
function parseYear(column) {
    const yearSplitIndex = 2
    const baseTen = 10

    return parseInt(column.trim().split(' ')[yearSplitIndex], baseTen)
}

/**
 * parseInputCSV - Builds up an object representation of the input csv file
 *
 * @param  {string} inputFilePath - file path of input csv
 * @returns {object}              - object of presidential data
 */
function parseInputCSV(inputFilePath) {
    const headerColumn = 1
    const parsed = parse(fs.readFileSync(inputFile, "utf8")).slice(headerColumn) // reads in our file, parses it and drops header
    let presidents = {}

    parsed.forEach(function(row) {
        const name = row[nameColumn].trim()
        const birthYear = parseYear(row[birthDateColumn])
        const deathYear = parseYear(row[deathDateColumn])

        presidents[name] = {}
        presidents[name][birthYearKey] = birthYear
        presidents[name][deathYearKey] = deathYear
    })

    return presidents
}

/**
 * presidentAliveInYear - Determines if a preseident was alive in a given year
 *
 * @param  {object} presidentObj - object of single president data
 * @param  {number} year         - year to check if a president was alive during
 * @returns {boolean}            - whether they were alive
 */
function presidentAliveInYear(presidentObj, year) {
    return (presidentObj.birthYear <= year) && (presidentObj.deathyear == "undefined" || presidentObj.deathYear >= year)
}

/**
 * presidentsAliveInYear - finds all presidents alive in a given year
 *
 * @param  {object} presidentsObj - object of presidents data
 * @param  {number} year          - year to check if presidentsObj was alive during
 * @returns {string[]}              - list of presidents alive during given year
 */
function presidentsAliveInYear(presidentsObj, year) {
    let alivePresidents = []

    for(const presidentName in presidentsObj) {
        if(presidentAliveInYear(presidentsObj[presidentName], year)) {
            alivePresidents.push(presidentName)
        }
    }

    return alivePresidents
}

/**
 * findEarliestYear - finds the earliest year in the dataset
 *
 * @param  {object} presidentsObj - object of all presidents data
 * @returns {number}              - earliest year in data set
 */
function findEarliestYear(presidentsObj) {
    let earliestYear = Number.MAX_SAFE_INTEGER

    for(const presidentName in presidentsObj) {
        const birthYear = presidentsObj[presidentName][birthYearKey]
        const deathYear = presidentsObj[presidentName][deathYearKey]

        if(birthYear < earliestYear) {
            earliestYear = birthYear
        }

        if (deathYear < earliestYear) {
            earliestYear = deathYear
        }
    }

    return earliestYear
}

/**
 * findLatestYear - finds latest year in data set
 *
 * @param  {object} presidentsObj - object of all presidents data
 * @returns {number}              - latest year in data set
 */
function findLatestYear(presidentsObj) {
    let latestYear = Number.MIN_SAFE_INTEGER

    for(const presidentName in presidentsObj) {
        const birthYear = presidentsObj[presidentName][birthYearKey]
        const deathYear = presidentsObj[presidentName][deathYearKey]

        if(birthYear > latestYear) {
            latestYear = birthYear
        }

        if (deathYear > latestYear) {
            latestYear = deathYear
        }
    }

    return latestYear}

/**
 * yearsWithMostLivingPresidents - Finds the years with the most presidents alive
 *
 * @param  {Object} presidentsObj - object of all presidents data
 * @returns {number[]}                - list of years with most presidents alive
 */
function yearsWithMostLivingPresidents(presidentsObj) {
    const earliestYear = findEarliestYear(presidentsObj)
    const latestYear = findLatestYear(presidentsObj)
    let presidentsAliveInYearsObj = {}

    for(let year = earliestYear; year <= latestYear; year++) {
        presidentsAliveInYearsObj[year] = presidentsAliveInYear(presidentsObj, year)
    }

    let yearsWithMostPresidentsAlive = []
    let mostPresidentsAlive = 0
    for(let year in presidentsAliveInYearsObj) {
        year = parseInt(year) // recasting to Int, as our keys are Strings
        const numberOfPresidentsAliveInYear = Object.keys(presidentsAliveInYearsObj[year]).length

        if(numberOfPresidentsAliveInYear == mostPresidentsAlive) {
            // add a new year, as we found a tie
            yearsWithMostPresidentsAlive.push(year)
        } else if(numberOfPresidentsAliveInYear > mostPresidentsAlive) {
            // clear our list and add this year, as we found a year with a greater count of alive presidents
            mostPresidentsAlive = numberOfPresidentsAliveInYear

            yearsWithMostPresidentsAlive = []
            yearsWithMostPresidentsAlive.push(year)
        }
    }

    return yearsWithMostPresidentsAlive
}

/**
 * findYearsWithMostLivingPresidents - parses input file and finds years with most living presidents
 *
 * @returns {number[]} - list of years with most presidents alive
 */
function findYearsWithMostLivingPresidents() {
    const presidentsObj = parseInputCSV(inputFile)
    return yearsWithMostLivingPresidents(presidentsObj)
}

const expected_output = [1822, 1823, 1824, 1825, 1826, 1831, 1833, 1834, 1835, 1836, 1837, 1838, 1839, 1840, 1841, 1843, 1844, 1845]
assert.deepStrictEqual(expected_output, findYearsWithMostLivingPresidents())
