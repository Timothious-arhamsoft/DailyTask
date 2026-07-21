
def square(rows):
    for i in range(rows):
        print("*" * rows)

def rectangle(rows, cols):
    for i in range(rows):
        print("*" * cols)


def pyramid(size):
    for i in range(1, size+1):
        print(" " * (size - i) + "*" * (2*i-1))

def right_angle(size):
    for i in range(1, size + 1):
        print("*"* i)


if __name__ == "__main__":
    print("--- Sqauare- --")
    square(5)
    print("--- Recatangle ---")
    rectangle(3,4)
    print("--- Pyramid ---")
    pyramid(5)
    print("--- Right Angle ---")
    right_angle(5)

