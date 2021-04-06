import sys


def main(lines):
    lines = list(lines.split())  # inputデータの箱
    stack = []  # listで行います
    jugh = True
    for i in lines:
        if i.isdigit():
            stack.append(i)
        else:
            if i == "+":
                if len(stack) >= 2:
                    value1, value2 = stack.pop(-2), stack.pop()
                    stack.append(value1+value2)
                else:
                    jugh = False

            if i == "-":
                if len(stack) >= 2:
                    value1, value2 = stack.pop(-2), stack.pop()
                    stack.append(value1-value2)
                else:
                    jugh = False

            if i == "*":
                if len(stack) >= 2:
                    value1, value2 = stack.pop(-2), stack.pop()
                    stack.append(value1 * value2)
                else:
                    jugh = False

            if i == "++":
                if len(stack) >= 1:
                    value1 = stack.pop()
                    stack.append(value1 + 1)
                else:
                    jugh = False

            if i == "@":
                if len(stack) >= 3:
                    value1, value2, value3 = stack.pop(
                        -3), stack.pop(-2), stack.pop()
                    stack.append(value1 * value2 + value2 *
                                 value3 + value3 * value1)
                else:
                    jugh = False
        if not jugh:
            print("invalid")
    print(stack.pop())



