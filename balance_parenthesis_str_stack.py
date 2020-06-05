from my_stack import Stack


def balance_per_str_with_stack(str1):
    s = Stack()
    balanced = True
    index = 0

    while index < len(str1) and balanced:
        symbol = str1[index]
        print(symbol, " : ", s)
        if symbol == "(":
            s.push(symbol)

        else: # 심볼이 ")"인 경우!
            if s.isEmpty():
                balanced = False
            else:
                # 스택 s에 "("가 있는 경우
                s.pop()
        index += 1
        print(s)

    if balanced and s.isEmpty():
        return True
    else:
        return False


if __name__ == "__main__":
    print(balance_per_str_with_stack('((()))'))
    print(balance_per_str_with_stack('(()'))