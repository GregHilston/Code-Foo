package main

import (
  "fmt"
  "strconv"
  "strings"
)

func persist(input int, iteration int) (int, int) {
  inputStr := strconv.Itoa(input)
  digits := strings.Split(inputStr, "")
  sum := 0
  for _, digit := range digits {
    myNum, _ := strconv.Atoi(digit)
    sum += myNum
  }
  iteration++
  if len(strconv.Itoa(sum)) > 1 {
    sum, iteration = persist(sum, iteration)
  }
  return sum, iteration
}

func main() {
  _, iterationCount := persist(199, 0)
  fmt.Println(iterationCount)
}