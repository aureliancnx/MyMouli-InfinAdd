import subprocess
import sys
from random import randrange
from time import sleep
import atexit

tests = 0

def exit_handler():
    print("\033[93m[MOULI] \x1b[0m{0} tests passés.".format(tests))

# Get the output from an executable
def get_output(args):
    popen = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    popen.wait(2)
    output = popen.stdout.read()
    return output.decode("utf-8")


# Compare two outputs
def compare(file_my, num1, num2):
    expected = str(num1 + num2)
    output = get_output((file_my, str(num1), str(num2)))
    global tests
    tests += 1

    if output != expected:
        print("\033[93m[MOULI] \x1b[0;30;41m{0} : Difference with args: {1} {2}\x1b[0m".format(file_my, str(num1), str(num2)))
        print("\033[93m[MOULI] Expected:\x1b[0m")
        print(expected)
        print("\033[93m[MOULI] But got:\x1b[0m")
        print(output)
        exit()
    else:
        print("\033[93m[MOULI] \x1b[0m{0} : Args: {1} {2} = PASSED.\x1b[0m".format(file_my, str(num1), str(num2)))

def randomizer():
    i = '1'
    neg = randrange(0, 10)
    for b in range(1, randrange(25)):
        i = i + str(randrange(0, 9))
    i = int(i)
    if neg <= 5:
        i *= -1
    return i

# Check file output differences
def check(file_origin):
    for x in range(1, 1000):
        for y in range(1, 1000):
            compare(file_origin, randomizer(), randomizer())


def main(argv):
    atexit.register(exit_handler)
    if len(sys.argv) != 2:
        print("\x1b[0mUsage: mouli_infadd.py <origin_file>")
        exit(1)

    print("\033[93m[MOULI] \x1b[0;30;44mRunning tests -> {0}...\x1b[0m".format(sys.argv[1]))
    sleep(1)
    check(sys.argv[1])
    print("\033[93m[MOULI] \x1b[6;30;42mEverything seems izoké.\x1b[0m")


if __name__ == "__main__":
    main(sys.argv[1:])