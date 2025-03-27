# 逆波兰表达式的实现


def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b),  # 整除
    }

    for t in tokens:
        if t in ops:
            a = stack.pop()
            b = stack.pop()
            stack.append(ops[t](a, b))
        else:
            stack.append(int(t))
    return stack[0]


# 计算 (3 + 5) * 2 => 16
tokens = ["3", "5", "+", "2", "*"]
print(eval_rpn(tokens))
