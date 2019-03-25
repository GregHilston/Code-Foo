def multiply(multiplicand: int, multiplier: int, sum: int):
  print(f"\tmultiply multiplicand {multiplicand} multiplier {multiplier} sum {sum}")

  if multiplier == 0:
    return sum

  new_sum = sum + multiplicand
  new_multiplier = multiplier - 1

  return multiply(multiplicand, new_multiplier, new_sum)

def recursive_multiply(multiplicand: int, multiplier: int):
  print(f"recursive_multiply multiplicand {multiplicand} multiplier {multiplier}")
  print(multiply(multiplicand, multiplier, 0))

recursive_multiply(5, 5)