from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    stack = MyStack()

    for char in string:
        if char == "(" or char == "[" or char == "{":
            stack.push(char)
        else:
            if len(stack) == 0:
                return False

            topo = stack.pop()

            if char == ")" and topo != "(":
                return False
            if char == "]" and topo != "[":
                return False
            if char == "}" and topo != "{":
                return False

    return len(stack) == 0
