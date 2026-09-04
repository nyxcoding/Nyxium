def eval(condition, variables):
    if "<=" in condition:
        left, right = condition.split("<=", 1)

        left = left.strip()
        right = right.strip()

        if left in variables:
            left = variables[left]

        try:
            return int(left) <= int(right)
        except ValueError:
            print(f"TypeError: parameter is not of type int")
    if ">=" in condition:
        left, right = condition.split(">=", 1)

        left = left.strip()
        right = right.strip()

        if left in variables:
            left = variables[left]
        try:
            return int(left) >= int(right)
        except ValueError:
            print(f"TypeError: parameter is not of type int")
    if "!=" in condition:
        left, right = condition.split("!=", 1)

        left = left.strip()
        right = right.strip()

        if left in variables:
            left = variables[left]

        return str(left) != right

    if "==" in condition:
        left, right = condition.split("==", 1)

        left = left.strip()
        right = right.strip()

        if left in variables:
            left = variables[left]
        
        return str(left) == right
    if ">" in condition:
        left, right = condition.split(">", 1)

        left = left.strip()
        right = right.strip()

        if left in variables:
            left = variables[left]

        try:
            return int(left) > int(right)
        except ValueError:
            print("TypeError: parameter is not of type int")

    if "<" in condition:
        left, right = condition.split("<", 1)

        left = left.strip()
        right = right.strip()

        if left in variables:
            left = variables[left]

        try:
            return int(left) < int(right)
        except ValueError:
            print(f"TypeError: parameter is not of type int")

    return False