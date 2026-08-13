import sys
def soleve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a = int(input_data[0])
    b = int(input_data[1])
    c = int(input_data[2])
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("Teng tomonli")
        elif a == b or b == c or a == c:
            print("Teng yonli")
        else:
            print("Turli tomonli")
    else:
        print("Uchburchak emas")
if __name__ == '__main__':
    soleve()