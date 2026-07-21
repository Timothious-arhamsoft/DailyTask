# -----------Task 1
#---- calling the pakage
import patterns
import dsa

def main():
    print("--- Pyramid ---")
    patterns.pyramid(5)

    print("--- Rectangle ---")
    patterns.rectangle(3, 4)

    print("----Second Pakage----")
    print("Factorial:")
    print(dsa.factorial(5))
    print("---- Sum of Numbers----")
    print("Original Val: 137")
    print(dsa.recursive_sum_of_num(137))

if __name__ == "__main__":

    main()