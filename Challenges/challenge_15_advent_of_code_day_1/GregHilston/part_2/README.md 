The first mistake I made was not looping over the input file multiple times. Once I figured that out, the second mistake I made was keeping my voltages in a python `list`. This, thanks to Thomas, has an `O(n)` lookup time and the runtime was a lot slower. Instead, I used a `dictionary` which has an `O(1)` lookup time.

## Hardware

MacBook Pro (Retina, 15-inch, Mid 2015)

Processor: 2.8 GHz Intel Core i7

Memory: 16 GB 1600 MHz DDR3

## Actual Run Times

### With `list`

 147.0985472202301 seconds

### With `dictionary`

0.10479402542114258 seconds

Which is 1403 times faster than the implementation with a `list`