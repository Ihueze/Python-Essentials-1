# ASCII Art Arrow in Python

## This script prints two versions of an ASCII art arrow using Python:

  ###  The **first arrow** is printed line by line using separate `print()` statements.
  #### The **second arrow** is a larger version, created using string multiplication and newline characters.

## First Arrow (Standard Size)

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


## Second Arrow (Larger Size)


print("    *    \n" * 2 +
      "   * *   \n" * 2 +
      " *** *** \n" * 2 +
      "   * *   \n" * 2 +
      "   * *   \n" * 2 +
      "   ***")