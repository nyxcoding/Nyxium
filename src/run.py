<<<<<<< HEAD
import errors
import functions
import time
import random

def run(code):
    variables = {}
    functionss = {}
    inside_if = False
    run_block = True
    loop_count = 0
    loop_start = 0
    line_index = 0
    maths = False
    wait = False
    random = False

    lines= code.splitlines()

    while line_index < len(lines):
        line = lines[line_index].strip()

        if inside_if and not run_block:
            if line == "end":
                inside_if = False
                run_block = True
            
            line_index += 1
            continue
        # SAY

        if line.startswith("say(") and line.endswith(")"):
            text = line[4:-1].strip()
            if text in variables:
                print((variables[text]))
            else:

                if text.startswith ('"') and text.endswith('"'):
                    print(text[1:-1])
                else:
                    errors.handle(line, 'Error: speech marks not found.')
        
        elif line.startswith("night ") and line.endswith("{"):
            name = line[6: -1].strip()
            
            function_lines = []
            function_start = line_index + 1
            
            while line_index < len(lines):
                function_line = lines[line_index]
                if function_line == "}":
                    break
                function_lines.append(function_line)
                line_index += 1
            functionss[name] = function_lines

        # INPUT

        elif line.startswith("input"):
            var = line[6: ].strip()
            variables[var] = input("> ")

        # VAR

        elif line.startswith("var") and '=' in line:
            statement = line[4:]

            if '=' not in statement:
                errors.handle(line, "Missing the '=' character in function var.")
                exit()

            name, value = statement.split("=", 1)

            name = name.strip()
            value = value.strip()

            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.isdigit():
                value = int(value)
                
            if isinstance(value, str) and '+'in value:
                left, right = value.split("+", 1)

                left = left.strip()
                right = right.strip()

                if left in variables:
                    left = variables[left]
                if right in variables:
                    right = variables[right]
                value = int(left) + int(right)

        
            elif isinstance(value, str) and '-' in value:
                left, right = value.split("-", 1)

                left = left.strip()
                right = right.strip()

                if left in variables:
                    left = variables[left]
                if right in variables:
                    right = variables[right]
            
                value = int(left) - int(right)

            elif isinstance(value, str) and '*' in value:
                left, right = value.split("*", 1)

                left = left.strip()
                right = right.strip()
                if left in variables:
                    left = variables[left]
                if right in variables:
                    right = variables[right]

                value = int(left) * int(right)   
        
            elif isinstance(value, str) and '/' in value:
                left, right = value.split("/", 1)

                left =  left.strip()
                right = right.strip()
                if right == 0:
                    print("Error: Cannot divide by 0")
                    exit()
                if left in variables:
                    left = variables[left] 
                if right in variables:
                    right = variables[right]
            
                value = int(left) / int(right)
            
            variables[name] = value

        # IF

        elif line.startswith("if"):
            statement = line[3: ]
            if functions.eval(statement, variables):
                run_block = True
            else:
                run_block = False
            inside_if = True
            line_index += 1
            continue

        # LOOP

        elif line.startswith("loop"):
            amount = int(line[4:].strip())
            loop_start = line_index + 1
            loop_count = amount
            line_index += 1
            continue

        # END
        elif line == "end":
            if inside_if == True:
                inside_if = False
                line_index += 1
                continue
            elif loop_count > 0:
                loop_count -= 1

                if loop_count > 0:
                    line_index = loop_start
                    continue
                line_index += 1
                continue

            else:
                errors.handle(line_index, "Statement not found.")

        # COMMENTS
        elif line.startswith('@'):
            line_index += 1
            continue

        # ALLOW NEW LINES
        elif line.strip() == "":
            line_index += 1
            continue

        elif line.startswith("add(") and line.endswith(")"):
            values = line[4: -1].split(",")
            if maths == True:

                left = values[0].strip()
                right = values[1].strip()

                if left in variables:
                    left = variables[left]
                if right in variables:
                    right = variables[right]
                left = int(left)
                right = int(right)
                sum = int(left) + int(right)

                print(sum)    
            else:
                errors.handle(line_index, "Math module not found, try using `get math`")

        elif line.startswith("subtract(") and line.endswith(")"):
            values = line[9: -1].split(",")
            if maths == True:

                left = values[0].strip()
                right = values[1].strip()

                if left in variables:
                    left = variables[left]
                if right in variables:
                    right = variables[right]
                left = int(left)
                right = int(right)
                sum = int(left) - int(right)

                print(sum)    
            else:
                errors.handle(line_index, "Math module not found, try using `get math`")

        elif line.startswith("multiply(") and line.endswith(")"):
            if maths == True:
                values = line[9:-1].split()

                left = values[0].split()
                right = values[1].split()

                if left in variables:
                    left = variables[left]
                if right in variables:
                    right = variables[right]

                sum = int(left) * int(right)

                print(sum)
            else:
                errors.handle(line_index, "Math module not found, try using `get math`")

        elif line.startswith("divide(") and line.endswith(")"):
            if maths == True:
                values = line[7:-1].split()

                left = values[0].split()
                right = values[1].split()

                if left in variables:
                    left = variables[left]
                if right in variables:
                    right = variables[right]
                if right == 0:
                    errors.handle(line_index, "Cannot divide by 0")

                sum = int(left) / int(right)

                print(sum)
            else:
                errors.handle(line_index, "Math module not found, try using `get math`")

        elif line.startswith("wait(") and line.endswith(")"):
            if wait == True:
                seconds = line[5: -1]
                seconds = int(seconds)
                time.sleep(seconds)
            else:
                errors.handle(line_index, "Wait module not found, try using `get wait`")
            
        elif line.startswith("randint(") and line.endswith(")"):
            if wait == True:
                ints = line[8: -1].split()
                
                intI = ints[0].split()
                intII = ints[1].split()
                
                if intI in variables:
                    intI = variables[intI]
                if intII in variables:
                    intII = variables[intII]
                rI = int(intI)
                rII = int(intII)
                num = random.randint(rI, rII)
                print(num)
            else:
                errors.handle(line_index, "Random module not found. Try using `get random`.")

        elif line.startswith("get"):
            lib = line[4:].strip()
            if lib == "math":
                maths = True
            elif lib == "wait":
                wait = True
            elif lib == "random":
                random = True
            else:
                errors.handle(line_index, "Library not found.")
            line_index += 1

        elif line.startswith("lose"):
            lib = line[4:].strip()
            if lib == "math":
                if maths == True:
                    maths = False
                else:
                    errors.handle(line_index, "Maths library already disabled!")
            elif lib == "wait":
                if wait == True:
                    wait = False
                else:
                    errors.handle(line_index, "Wait library already disabled!")
            elif lib == "random":
                if random == True:
                    random = False
                else:
                    errors.handle(line_index, "Random library already disabled.")
            else:
                errors.handle(line_index, "Invalid library")
        
        elif line.endswith("()"):
            name = line[:-2]
            if name in functionss:
                run("\n".join(functionss[name]))
            else:
                errors.handle(line_index, f"Function {name} not found.")
                
        else:
            print(f"Unknown command: Line {line_index + 1}")
        
        line_index += 1
=======
import errors
import functions
import time
import os
import random
import subprocess
import disc
import shutil


# ============================================================
# HELPERS
# ============================================================

def split_arguments(text, separator=","):
    """
    Splits arguments while respecting:
    - strings
    - parentheses
    - square brackets
    - braces

    Example:
        split_arguments('"hello, world", [1, 2, 3]')

    becomes:
        ['"hello, world"', '[1, 2, 3]']
    """

    parts = []
    current = []

    depth_paren = 0
    depth_square = 0
    depth_brace = 0

    in_string = False
    escaped = False

    for char in text:

        if escaped:

            current.append(char)
            escaped = False
            continue

        if char == "\\" and in_string:

            current.append(char)
            escaped = True
            continue

        if char == '"':

            in_string = not in_string
            current.append(char)
            continue

        if not in_string:

            if char == "(":
                depth_paren += 1

            elif char == ")":
                depth_paren -= 1

            elif char == "[":
                depth_square += 1

            elif char == "]":
                depth_square -= 1

            elif char == "{":
                depth_brace += 1

            elif char == "}":
                depth_brace -= 1

        if (
            char == separator
            and not in_string
            and depth_paren == 0
            and depth_square == 0
            and depth_brace == 0
        ):

            parts.append(
                "".join(current).strip()
            )

            current = []

        else:

            current.append(char)

    if current or text:

        parts.append(
            "".join(current).strip()
        )

    return parts


def find_matching_brace(lines, start_index):
    """
    Finds the } matching the { on lines[start_index].

    Supports nested blocks.
    """

    depth = 0
    in_string = False
    escaped = False

    for index in range(
        start_index,
        len(lines)
    ):

        line = lines[index]

        for char in line:

            if escaped:

                escaped = False
                continue

            if char == "\\" and in_string:

                escaped = True
                continue

            if char == '"':

                in_string = not in_string
                continue

            if not in_string:

                if char == "{":

                    depth += 1

                elif char == "}":

                    depth -= 1

                    if depth == 0:

                        return index

    return None


def clean_lines(code):
    """
    Converts source code into individual lines.

    Unlike the previous get_statements() implementation,
    this deliberately does NOT merge brace blocks together.

    That means:

        night test() {
            say("hello")
        }

    stays as three separate lines.
    """

    return code.splitlines()


def strip_quotes(value):

    value = value.strip()

    if (
        len(value) >= 2
        and value.startswith('"')
        and value.endswith('"')
    ):

        return value[1:-1]

    return value


def is_number(value):

    value = value.strip()

    if value.startswith("-"):

        value = value[1:]

    if value.isdigit():

        return True

    try:

        float(value)
        return True

    except ValueError:

        return False


def resolve_number(value, variables):

    value = value.strip()

    if value in variables:

        value = variables[value]

    if isinstance(value, bool):

        return int(value)

    return float(value) if "." in str(value) else int(value)


# ============================================================
# EXPRESSION / VALUE HANDLING
# ============================================================

def resolve_list(value, variables, modules, line_index):
    """
    Handles:

        [1, 2, 3]
        ["a", "b", "c"]
        [name, 123, "hello"]
    """

    content = value[1:-1].strip()

    if not content:

        return []

    parts = split_arguments(content)

    result = []

    for part in parts:

        result.append(
            resolve_value(
                part,
                variables,
                modules,
                line_index
            )
        )

    return result


def resolve_index(expression, variables, modules, line_index):

    bracket = expression.find("[")

    if bracket == -1:
        return None

    if not expression.endswith("]"):
        return None

    object_name = expression[:bracket].strip()

    index_expression = expression[
        bracket + 1:-1
    ].strip()

    if object_name not in variables:

        errors.handle(
            line_index,
            f"Variable '{object_name}' not found."
        )

        return None

    collection = variables[object_name]

    index = resolve_value(
        index_expression,
        variables,
        modules,
        line_index
    )

    try:

        return collection[int(index)]

    except (
        IndexError,
        KeyError,
        TypeError,
        ValueError
    ):

        errors.handle(
            line_index,
            "Invalid index."
        )

        return None


def evaluate_method(
    expression,
    variables,
    modules,
    line_index
):

    expression = expression.strip()

    # --------------------------------------------------------
    # FIND METHOD DOT
    # --------------------------------------------------------

    dot = -1
    depth = 0
    in_string = False

    for index, char in enumerate(expression):

        if char == '"':

            in_string = not in_string

        if in_string:
            continue

        if char == "(":

            depth += 1

        elif char == ")":

            depth -= 1

        elif char == "." and depth == 0:

            dot = index
            break

    if dot == -1:

        return None, False

    object_expression = expression[:dot].strip()
    method_expression = expression[dot + 1:].strip()

    if not method_expression.endswith(")"):

        return None, False

    open_paren = method_expression.find("(")

    if open_paren == -1:

        return None, False

    method_name = method_expression[
        :open_paren
    ].strip()

    argument_text = method_expression[
        open_paren + 1:-1
    ].strip()

    if argument_text:

        arguments = split_arguments(
            argument_text
        )

    else:

        arguments = []

    # --------------------------------------------------------
    # MODULE FUNCTION
    # --------------------------------------------------------

    if object_expression in modules:

        module = modules[
            object_expression
        ]

        if not isinstance(module, dict):

            errors.handle(
                line_index,
                f"Module '{object_expression}' does not expose functions."
            )

            return None, True

        module_functions = module.get(
            "functions",
            {}
        )

        if method_name not in module_functions:

            errors.handle(
                line_index,
                f"Function '{method_name}' not found in module "
                f"{object_expression}."
            )

            return None, True

        function = module_functions[
            method_name
        ]

        parameters = function[
            "parameters"
        ]

        body = function[
            "body"
        ]

        if len(arguments) != len(parameters):

            errors.handle(
                line_index,
                f"Function {method_name} expects "
                f"{len(parameters)} argument(s), "
                f"got {len(arguments)}."
            )

            return None, True

        local_variables = module[
            "variables"
        ].copy()

        for parameter, argument in zip(
            parameters,
            arguments
        ):

            local_variables[
                parameter
            ] = resolve_value(
                argument,
                variables,
                modules,
                line_index
            )

        result = run(
            "\n".join(body),
            local_variables,
            functionss=module_functions,
            modules=modules
        )

        return result, True

    # --------------------------------------------------------
    # OBJECT VALUE
    # --------------------------------------------------------

    object_value = resolve_value(
        object_expression,
        variables,
        modules,
        line_index
    )

    # --------------------------------------------------------
    # STRING METHODS
    # --------------------------------------------------------

    if isinstance(object_value, str):

        if method_name == "split":

            separator = None

            if arguments:

                separator = resolve_value(
                    arguments[0],
                    variables,
                    modules,
                    line_index
                )

            return object_value.split(
                separator
            ), True

        if method_name == "strip":

            return object_value.strip(), True

        if method_name == "lower":

            return object_value.lower(), True

        if method_name == "upper":

            return object_value.upper(), True

        if method_name == "capitalize":

            return object_value.capitalize(), True

        if method_name == "replace":

            if len(arguments) != 2:

                errors.handle(
                    line_index,
                    ".replace() requires 2 arguments."
                )

                return None, True

            old = resolve_value(
                arguments[0],
                variables,
                modules,
                line_index
            )

            new = resolve_value(
                arguments[1],
                variables,
                modules,
                line_index
            )

            return object_value.replace(
                str(old),
                str(new)
            ), True

        if method_name == "startswith":

            if len(arguments) != 1:

                errors.handle(
                    line_index,
                    ".startswith() requires 1 argument."
                )

                return None, True

            prefix = resolve_value(
                arguments[0],
                variables,
                modules,
                line_index
            )

            return object_value.startswith(
                str(prefix)
            ), True

        if method_name == "endswith":

            if len(arguments) != 1:

                errors.handle(
                    line_index,
                    ".endswith() requires 1 argument."
                )

                return None, True

            suffix = resolve_value(
                arguments[0],
                variables,
                modules,
                line_index
            )

            return object_value.endswith(
                str(suffix)
            ), True

        if method_name == "contains":

            if len(arguments) != 1:

                errors.handle(
                    line_index,
                    ".contains() requires 1 argument."
                )

                return None, True

            item = resolve_value(
                arguments[0],
                variables,
                modules,
                line_index
            )

            return item in object_value, True

        if method_name == "length":

            if arguments:

                errors.handle(
                    line_index,
                    ".length() takes no arguments."
                )

                return None, True

            return len(object_value), True

    # --------------------------------------------------------
    # LIST METHODS
    # --------------------------------------------------------

    if isinstance(object_value, list):

        if method_name == "append":

            if len(arguments) != 1:

                errors.handle(
                    line_index,
                    ".append() requires 1 argument."
                )

                return None, True

            item = resolve_value(
                arguments[0],
                variables,
                modules,
                line_index
            )

            object_value.append(item)

            return None, True

        if method_name == "extend":

            if len(arguments) != 1:

                errors.handle(
                    line_index,
                    ".extend() requires 1 argument."
                )

                return None, True

            item = resolve_value(
                arguments[0],
                variables,
                modules,
                line_index
            )

            if not isinstance(item, list):

                errors.handle(
                    line_index,
                    ".extend() requires a list."
                )

                return None, True

            object_value.extend(item)

            return None, True

        if method_name == "insert":

            if len(arguments) != 2:

                errors.handle(
                    line_index,
                    ".insert() requires 2 arguments."
                )

                return None, True

            index = resolve_value(
                arguments[0],
                variables,
                modules,
                line_index
            )

            item = resolve_value(
                arguments[1],
                variables,
                modules,
                line_index
            )

            object_value.insert(
                int(index),
                item
            )

            return None, True

        if method_name == "remove":

            if len(arguments) != 1:

                errors.handle(
                    line_index,
                    ".remove() requires 1 argument."
                )

                return None, True

            item = resolve_value(
                arguments[0],
                variables,
                modules,
                line_index
            )

            try:

                object_value.remove(item)

            except ValueError:

                errors.handle(
                    line_index,
                    "Item not found in list."
                )

            return None, True

        if method_name == "pop":

            if len(arguments) > 1:

                errors.handle(
                    line_index,
                    ".pop() accepts zero or one argument."
                )

                return None, True

            try:

                if arguments:

                    index = resolve_value(
                        arguments[0],
                        variables,
                        modules,
                        line_index
                    )

                    return object_value.pop(
                        int(index)
                    ), True

                return object_value.pop(), True

            except IndexError:

                errors.handle(
                    line_index,
                    "Cannot pop from an empty list."
                )

                return None, True

        if method_name == "clear":

            if arguments:

                errors.handle(
                    line_index,
                    ".clear() takes no arguments."
                )

                return None, True

            object_value.clear()

            return None, True

        if method_name == "length":

            return len(object_value), True

        if method_name == "contains":

            if len(arguments) != 1:

                errors.handle(
                    line_index,
                    ".contains() requires 1 argument."
                )

                return None, True

            item = resolve_value(
                arguments[0],
                variables,
                modules,
                line_index
            )

            return item in object_value, True

    errors.handle(
        line_index,
        f"Unknown method '{method_name}'."
    )

    return None, True


def resolve_value(
    value,
    variables,
    modules,
    line_index
):

    value = value.strip()

    # --------------------------------------------------------
    # EMPTY
    # --------------------------------------------------------

    if value == "":

        return ""

    # --------------------------------------------------------
    # STRING
    # --------------------------------------------------------

    if (
        len(value) >= 2
        and value.startswith('"')
        and value.endswith('"')
    ):

        return value[1:-1]

    # --------------------------------------------------------
    # BOOLEAN
    # --------------------------------------------------------

    if value == "true":

        return True

    if value == "false":

        return False

    # --------------------------------------------------------
    # LIST
    # --------------------------------------------------------

    if (
        value.startswith("[")
        and value.endswith("]")
    ):

        return resolve_list(
            value,
            variables,
            modules,
            line_index
        )

    # --------------------------------------------------------
    # METHOD CALL
    # --------------------------------------------------------

    if "." in value and value.endswith(")"):

        result, handled = evaluate_method(
            value,
            variables,
            modules,
            line_index
        )

        if handled:

            return result

    # --------------------------------------------------------
    # INDEX
    # --------------------------------------------------------

    if (
        "[" in value
        and value.endswith("]")
    ):

        result = resolve_index(
            value,
            variables,
            modules,
            line_index
        )

        if result is not None:

            return result

    # --------------------------------------------------------
    # INTEGER / FLOAT
    # --------------------------------------------------------

    if is_number(value):

        try:

            if "." in value:

                return float(value)

            return int(value)

        except ValueError:

            pass

    # --------------------------------------------------------
    # VARIABLE
    # --------------------------------------------------------

    if value in variables:

        return variables[value]

    # --------------------------------------------------------
    # ADDITION / CONCATENATION
    # --------------------------------------------------------

    parts = split_arguments(
        value,
        "+"
    )

    if len(parts) > 1:

        result = resolve_value(
            parts[0],
            variables,
            modules,
            line_index
        )

        for part in parts[1:]:

            right = resolve_value(
                part,
                variables,
                modules,
                line_index
            )

            if (
                isinstance(result, str)
                or isinstance(right, str)
            ):

                result = (
                    str(result)
                    + str(right)
                )

            else:

                result += right

        return result

    # --------------------------------------------------------
    # MULTIPLICATION
    # --------------------------------------------------------

    parts = split_arguments(
        value,
        "*"
    )

    if len(parts) > 1:

        result = resolve_value(
            parts[0],
            variables,
            modules,
            line_index
        )

        for part in parts[1:]:

            right = resolve_value(
                part,
                variables,
                modules,
                line_index
            )

            result *= right

        return result

    # --------------------------------------------------------
    # DIVISION
    # --------------------------------------------------------

    parts = split_arguments(
        value,
        "/"
    )

    if len(parts) > 1:

        result = resolve_value(
            parts[0],
            variables,
            modules,
            line_index
        )

        for part in parts[1:]:

            right = resolve_value(
                part,
                variables,
                modules,
                line_index
            )

            if right == 0:

                errors.handle(
                    line_index,
                    "Cannot divide by 0."
                )

                return None

            result /= right

        return result

    # --------------------------------------------------------
    # SUBTRACTION
    # --------------------------------------------------------

    parts = split_arguments(
        value,
        "-"
    )

    if (
        len(parts) > 1
        and value[0] != "-"
    ):

        result = resolve_value(
            parts[0],
            variables,
            modules,
            line_index
        )

        for part in parts[1:]:

            right = resolve_value(
                part,
                variables,
                modules,
                line_index
            )

            result -= right

        return result

    # --------------------------------------------------------
    # RAW VALUE
    # --------------------------------------------------------

    return value


# ============================================================
# CONDITIONS
# ============================================================

def evaluate_condition(
    condition,
    variables,
    modules,
    line_index
):

    condition = condition.strip()

    # --------------------------------------------------------
    # TRY EXISTING NYXIUM EVALUATOR FIRST
    # --------------------------------------------------------

    try:

        result = functions.eval(
            condition,
            variables
        )

        if isinstance(result, bool):

            return result

    except Exception:

        pass

    # --------------------------------------------------------
    # COMMON COMPARATORS
    # --------------------------------------------------------

    operators = [
        "==",
        "!=",
        ">=",
        "<=",
        ">",
        "<"
    ]

    for operator in operators:

        parts = split_comparison(
            condition,
            operator
        )

        if parts is not None:

            left = resolve_value(
                parts[0],
                variables,
                modules,
                line_index
            )

            right = resolve_value(
                parts[1],
                variables,
                modules,
                line_index
            )

            if operator == "==":
                return left == right

            if operator == "!=":
                return left != right

            if operator == ">=":
                return left >= right

            if operator == "<=":
                return left <= right

            if operator == ">":
                return left > right

            if operator == "<":
                return left < right

    value = resolve_value(
        condition,
        variables,
        modules,
        line_index
    )

    return bool(value)


def split_comparison(text, operator):

    in_string = False
    depth = 0

    index = 0

    while index <= len(text) - len(operator):

        char = text[index]

        if char == '"':

            in_string = not in_string

        if not in_string:

            if char in "([{":

                depth += 1

            elif char in ")]}":

                depth -= 1

            if (
                depth == 0
                and text[index:index + len(operator)]
                == operator
            ):

                return (
                    text[:index].strip(),
                    text[
                        index + len(operator):
                    ].strip()
                )

        index += 1

    return None


# ============================================================
# FUNCTION HELPERS
# ============================================================

def parse_function(
    lines,
    start_index,
    line_index
):

    declaration = lines[
        start_index
    ].strip()

    declaration = declaration[
        6:-1
    ].strip()

    if (
        "(" not in declaration
        or not declaration.endswith(")")
    ):

        errors.handle(
            line_index,
            "Invalid function declaration."
        )

        return None, start_index

    name, args = declaration.split(
        "(",
        1
    )

    name = name.strip()

    args = args[:-1].strip()

    if args:

        parameters = [
            arg.strip()
            for arg in split_arguments(args)
        ]

    else:

        parameters = []

    end_index = find_matching_brace(
        lines,
        start_index
    )

    if end_index is None:

        errors.handle(
            line_index,
            f"Function '{name}' is missing '}}'."
        )

        return None, start_index

    body = lines[
        start_index + 1:end_index
    ]

    return {
        "name": name,
        "parameters": parameters,
        "body": body
    }, end_index


def call_function(
    function,
    args,
    variables,
    modules,
    functionss,
    line_index
):

    parameters = function[
        "parameters"
    ]

    body = function[
        "body"
    ]

    if args.strip():

        arguments = split_arguments(
            args
        )

    else:

        arguments = []

    if len(arguments) != len(parameters):

        errors.handle(
            line_index,
            f"Function expects "
            f"{len(parameters)} argument(s), "
            f"got {len(arguments)}."
        )

        return None

    local_variables = variables.copy()

    for parameter, argument in zip(
        parameters,
        arguments
    ):

        local_variables[
            parameter
        ] = resolve_value(
            argument,
            variables,
            modules,
            line_index
        )

    return run(
        "\n".join(body),
        local_variables,
        functionss=functionss,
        modules=modules
    )


# ============================================================
# MODULE LOADING
# ============================================================

def load_module(
    filename,
    alias,
    variables,
    modules,
    state,
    line_index
):

    if not filename.endswith(".nyx"):

        filename += ".nyx"

    if not os.path.isfile(filename):

        errors.handle(
            line_index,
            f"Library '{filename}' not found."
        )

        return False

    try:

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as f:

            module_code = f.read()

    except OSError as e:

        errors.handle(
            line_index,
            f"Could not load library '{filename}': {e}"
        )

        return False

    # --------------------------------------------------------
    # CREATE MODULE NAMESPACE
    # --------------------------------------------------------

    module_variables = {}

    module_functions = {}

    module = {
        "file": filename,
        "variables": module_variables,
        "functions": module_functions
    }

    modules[alias] = module

    # --------------------------------------------------------
    # RUN THE MODULE
    #
    # IMPORTANT:
    # state is shared.
    #
    # Therefore:
    #
    # ping.nyx:
    #     get discord
    #     client.slash(...)
    #
    # main.nyx:
    #     get ping
    #     client.run(...)
    #
    # uses the SAME discord state.
    # --------------------------------------------------------

    run(
        module_code,
        module_variables,
        functionss=module_functions,
        modules=modules,
        state=state
    )

    return True


# ============================================================
# MAIN INTERPRETER
# ============================================================

def run(
    code,
    variables=None,
    functionss=None,
    modules=None,
    state=None
):

    if variables is None:

        variables = {}

    if functionss is None:

        functionss = {}

    if modules is None:

        modules = {}

    if state is None:

        state = {
            "math": False,
            "wait": False,
            "random": False,
            "discord": False,
            "gui": False
        }

    lines = clean_lines(code)

    line_index = 0

    # --------------------------------------------------------
    # EXECUTION CONTROL
    # --------------------------------------------------------

    return_value = None

    while line_index < len(lines):

        raw_line = lines[line_index]

        line = raw_line.strip()

        # ----------------------------------------------------
        # EMPTY
        # ----------------------------------------------------

        if not line:

            line_index += 1
            continue

        # ----------------------------------------------------
        # COMMENTS
        # ----------------------------------------------------

        if line.startswith("@"):

            line_index += 1
            continue

        # ----------------------------------------------------
        # FUNCTION DECLARATION
        # ----------------------------------------------------

        if (
            line.startswith("night ")
            and line.endswith("{")
        ):

            function, end_index = parse_function(
                lines,
                line_index,
                line_index
            )

            if function is not None:

                functionss[
                    function["name"]
                ] = {
                    "parameters":
                        function["parameters"],

                    "body":
                        function["body"]
                }

            line_index = end_index + 1
            continue

        # ----------------------------------------------------
        # FOR LOOP
        #
        # for item in list {
        #     ...
        # }
        #
        # for i in 5 {
        #     ...
        # }
        # ----------------------------------------------------

        if (
            line.startswith("for ")
            and line.endswith("{")
        ):

            declaration = line[
                4:-1
            ].strip()

            if " in " not in declaration:

                errors.handle(
                    line_index,
                    "Invalid for loop. Use: for variable in value {"
                )

                line_index += 1
                continue

            variable_name, expression = (
                declaration.split(
                    " in ",
                    1
                )
            )

            variable_name = variable_name.strip()
            expression = expression.strip()

            if not variable_name.isidentifier():

                errors.handle(
                    line_index,
                    "Invalid for loop variable."
                )

                line_index += 1
                continue

            end_index = find_matching_brace(
                lines,
                line_index
            )

            if end_index is None:

                errors.handle(
                    line_index,
                    "For loop is missing '}'."
                )

                return return_value

            iterable = resolve_value(
                expression,
                variables,
                modules,
                line_index
            )

            # ------------------------------------------------
            # INTEGER = RANGE
            # ------------------------------------------------

            if isinstance(iterable, int):

                iterable = range(
                    iterable
                )

            elif isinstance(iterable, float):

                iterable = range(
                    int(iterable)
                )

            # ------------------------------------------------
            # NON-ITERABLE
            # ------------------------------------------------

            try:

                iterator = list(iterable)

            except TypeError:

                errors.handle(
                    line_index,
                    "Value cannot be used in a for loop."
                )

                line_index = end_index + 1
                continue

            body = lines[
                line_index + 1:end_index
            ]

            broken = False

            for item in iterator:

                variables[
                    variable_name
                ] = item

                result = run(
                    "\n".join(body),
                    variables,
                    functionss=functionss,
                    modules=modules,
                    state=state
                )

                if isinstance(
                    result,
                    dict
                ):

                    if result.get(
                        "break"
                    ):

                        broken = True
                        break

                    if result.get(
                        "return"
                    ):

                        return result

            line_index = end_index + 1
            continue

        # ----------------------------------------------------
        # WHILE LOOP
        #
        # while condition {
        #     ...
        # }
        # ----------------------------------------------------

        if (
            line.startswith("while ")
            and line.endswith("{")
        ):

            condition = line[
                6:-1
            ].strip()

            end_index = find_matching_brace(
                lines,
                line_index
            )

            if end_index is None:

                errors.handle(
                    line_index,
                    "While loop is missing '}'."
                )

                return return_value

            body = lines[
                line_index + 1:end_index
            ]

            safety_counter = 0
            broken = False

            while evaluate_condition(
                condition,
                variables,
                modules,
                line_index
            ):

                safety_counter += 1

                # ------------------------------------------------
                # PROTECTION AGAINST ACCIDENTAL INFINITE LOOPS
                # ------------------------------------------------

                if safety_counter > 100000:

                    errors.handle(
                        line_index,
                        "While loop exceeded 100000 iterations."
                    )

                    break

                result = run(
                    "\n".join(body),
                    variables,
                    functionss=functionss,
                    modules=modules,
                    state=state
                )

                if isinstance(
                    result,
                    dict
                ):

                    if result.get(
                        "break"
                    ):

                        broken = True
                        break

                    if result.get(
                        "return"
                    ):

                        return result

            line_index = end_index + 1
            continue

        # ----------------------------------------------------
        # BREAK
        # ----------------------------------------------------

        if line == "break":

            return {
                "break": True
            }

        # ----------------------------------------------------
        # CONTINUE
        # ----------------------------------------------------

        if line == "continue":

            return {
                "continue": True
            }

        # ----------------------------------------------------
        # RETURN
        # ----------------------------------------------------

        if line == "return":

            return {
                "return": True,
                "value": None
            }

        if line.startswith("return "):

            value = resolve_value(
                line[7:].strip(),
                variables,
                modules,
                line_index
            )

            return {
                "return": True,
                "value": value
            }

        # ----------------------------------------------------
        # IF
        # ----------------------------------------------------

        if line.startswith("if "):

            condition = line[
                3:
            ].strip()

            result = evaluate_condition(
                condition,
                variables,
                modules,
                line_index
            )

            if result:

                line_index += 1
                continue

            # skip until elsif / else / end

            depth = 0
            search_index = line_index + 1

            while search_index < len(lines):

                current = lines[
                    search_index
                ].strip()

                if current.startswith("if "):

                    depth += 1

                elif current == "end":

                    if depth == 0:

                        line_index = search_index + 1
                        break

                    depth -= 1

                elif (
                    depth == 0
                    and current.startswith("elsif ")
                ):

                    condition = current[
                        6:
                    ].strip()

                    if evaluate_condition(
                        condition,
                        variables,
                        modules,
                        search_index
                    ):

                        line_index = search_index + 1
                        break

                elif (
                    depth == 0
                    and current == "else"
                ):

                    line_index = search_index + 1
                    break

                search_index += 1

            continue

        # ----------------------------------------------------
        # ELSIF
        # ----------------------------------------------------

        if line.startswith("elsif "):

            # If execution reaches an elsif normally,
            # the previous if branch already handled it.

            line_index += 1
            continue

        # ----------------------------------------------------
        # ELSE
        # ----------------------------------------------------

        if line == "else":

            # Same idea as elsif.
            line_index += 1
            continue

        # ----------------------------------------------------
        # END
        # ----------------------------------------------------

        if line == "end":

            line_index += 1
            continue

        # ----------------------------------------------------
        # SAY
        # ----------------------------------------------------

        if (
            line.startswith("say(")
            and line.endswith(")")
        ):

            content = line[
                4:-1
            ].strip()

            parts = split_arguments(
                content
            )

            output = []

            for part in parts:

                value = resolve_value(
                    part,
                    variables,
                    modules,
                    line_index
                )

                output.append(
                    str(value)
                )

            print(
                " ".join(output)
            )

            line_index += 1
            continue

        # ----------------------------------------------------
        # INPUT
        # ----------------------------------------------------

        if line.startswith("input"):

            variable_name = line[
                5:
            ].strip()

            if not variable_name:

                errors.handle(
                    line_index,
                    "input requires a variable."
                )

            else:

                variables[
                    variable_name
                ] = input("> ")

            line_index += 1
            continue

        # ----------------------------------------------------
        # VAR
        # ----------------------------------------------------

        if (
            line.startswith("var ")
            and "=" in line
        ):

            statement = line[
                4:
            ]

            name, value = statement.split(
                "=",
                1
            )

            name = name.strip()
            value = value.strip()

            if not name.isidentifier():

                errors.handle(
                    line_index,
                    "Invalid variable name."
                )

                line_index += 1
                continue

            variables[name] = resolve_value(
                value,
                variables,
                modules,
                line_index
            )

            line_index += 1
            continue

        # ----------------------------------------------------
        # GET
        # ----------------------------------------------------

        if line.startswith("get "):

            statement = line[
                4:
            ].strip()

            parts = statement.split()

            if not parts:

                errors.handle(
                    line_index,
                    "get requires a library."
                )

                line_index += 1
                continue

            lib = parts[0]
            alias = lib

            if (
                len(parts) == 3
                and parts[1] == "with"
            ):

                alias = parts[2]

                if not alias.isidentifier():

                    errors.handle(
                        line_index,
                        "Invalid module alias."
                    )

                    line_index += 1
                    continue

            elif len(parts) != 1:

                errors.handle(
                    line_index,
                    "Invalid get syntax."
                )

                line_index += 1
                continue

            # ------------------------------------------------
            # BUILT-IN MODULES
            # ------------------------------------------------

            if lib == "math":

                modules[
                    alias
                ] = {
                    "builtin": "math"
                }

                state[
                    "math"
                ] = True

            elif lib == "discord":

                modules[
                    alias
                ] = {
                    "builtin": "discord"
                }

                state[
                    "discord"
                ] = True

            elif lib == "wait":

                modules[
                    alias
                ] = {
                    "builtin": "wait"
                }

                state[
                    "wait"
                ] = True

            elif lib == "random":

                modules[
                    alias
                ] = {
                    "builtin": "random"
                }

                state[
                    "random"
                ] = True

            # ------------------------------------------------
            # CUSTOM MODULE
            # ------------------------------------------------

            else:

                load_module(
                    lib,
                    alias,
                    variables,
                    modules,
                    state,
                    line_index
                )

            line_index += 1
            continue

        # ----------------------------------------------------
        # LOSE
        # ----------------------------------------------------

        if line.startswith("lose "):

            lib = line[
                5:
            ].strip()

            if lib in modules:

                del modules[
                    lib
                ]

                if lib == "math":
                    state["math"] = False

                elif lib == "discord":
                    state["discord"] = False

                elif lib == "wait":
                    state["wait"] = False

                elif lib == "random":
                    state["random"] = False

                elif lib == "gui":
                    state["gui"] = False

            elif lib == "math":

                if state["math"]:

                    state["math"] = False

                else:

                    errors.handle(
                        line_index,
                        "Maths library already disabled!"
                    )

            elif lib == "wait":

                if state["wait"]:

                    state["wait"] = False

                else:

                    errors.handle(
                        line_index,
                        "Wait library already disabled!"
                    )

            elif lib == "random":

                if state["random"]:

                    state["random"] = False

                else:

                    errors.handle(
                        line_index,
                        "Random library already disabled."
                    )

            else:

                errors.handle(
                    line_index,
                    "Invalid library."
                )

            line_index += 1
            continue

        # ----------------------------------------------------
        # READ
        #
        # read("file.txt")
        #
        # or:
        #
        # read("file.txt"; contents)
        # ----------------------------------------------------

        if (
            line.startswith("read(")
            and line.endswith(")")
        ):

            content = line[
                5:-1
            ].strip()

            parts = split_arguments(
                content,
                ";"
            )

            if len(parts) not in (
                1,
                2
            ):

                errors.handle(
                    line_index,
                    "read() requires a filename and optionally a variable."
                )

                line_index += 1
                continue

            filename = resolve_value(
                parts[0],
                variables,
                modules,
                line_index
            )

            try:

                with open(
                    str(filename),
                    "r",
                    encoding="utf-8"
                ) as f:

                    contents = f.read()

                if len(parts) == 2:

                    variable_name = parts[
                        1
                    ].strip()

                    if not variable_name.isidentifier():

                        errors.handle(
                            line_index,
                            "Invalid variable name for read()."
                        )

                    else:

                        variables[
                            variable_name
                        ] = contents

                else:

                    print(
                        contents,
                        end=""
                    )

            except FileNotFoundError:

                errors.handle(
                    line_index,
                    f"File '{filename}' not found."
                )

            except OSError as e:

                errors.handle(
                    line_index,
                    f"Could not read file: {e}"
                )

            line_index += 1
            continue

        # ----------------------------------------------------
        # OPEN
        # ----------------------------------------------------

        if (
            line.startswith("open(")
            and line.endswith(")")
        ):

            filename = resolve_value(
                line[5:-1],
                variables,
                modules,
                line_index
            )

            try:

                state[
                    "file"
                ] = open(
                    str(filename),
                    "w",
                    encoding="utf-8"
                )

            except OSError as e:

                errors.handle(
                    line_index,
                    f"Could not open file: {e}"
                )

            line_index += 1
            continue

        # ----------------------------------------------------
        # WRITE
        # ----------------------------------------------------

        if (
            line.startswith("write(")
            and line.endswith(")")
        ):

            file = state.get(
                "file"
            )

            if file is None:

                errors.handle(
                    line_index,
                    "No file is open."
                )

            else:

                value = resolve_value(
                    line[6:-1],
                    variables,
                    modules,
                    line_index
                )

                file.write(
                    str(value)
                )

                file.write(
                    "\n"
                )

                file.flush()

            line_index += 1
            continue

        # ----------------------------------------------------
        # NEWDIR
        # ----------------------------------------------------

        if (
            line.startswith("newdir(")
            and line.endswith(")")
        ):

            dirname = resolve_value(
                line[7:-1],
                variables,
                modules,
                line_index
            )

            try:

                os.makedirs(
                    str(dirname),
                    exist_ok=True
                )

            except OSError as e:

                errors.handle(
                    line_index,
                    f"Could not create directory: {e}"
                )

            line_index += 1
            continue

        # ----------------------------------------------------
        # WAIT
        # ----------------------------------------------------

        if (
            line.startswith("wait(")
            and line.endswith(")")
        ):

            if not state["wait"]:

                errors.handle(
                    line_index,
                    "Wait module not found, try using `get wait`"
                )

            else:

                seconds = resolve_value(
                    line[5:-1],
                    variables,
                    modules,
                    line_index
                )

                time.sleep(
                    float(seconds)
                )

            line_index += 1
            continue

        # ----------------------------------------------------
        # RANDOM
        # ----------------------------------------------------

        if (
            line.startswith("randint(")
            and line.endswith(")")
        ):

            if not state["random"]:

                errors.handle(
                    line_index,
                    "Random module not found. Try using `get random`."
                )

            else:

                values = split_arguments(
                    line[8:-1]
                )

                if len(values) != 2:

                    errors.handle(
                        line_index,
                        "randint() requires 2 arguments."
                    )

                else:

                    first = resolve_value(
                        values[0],
                        variables,
                        modules,
                        line_index
                    )

                    second = resolve_value(
                        values[1],
                        variables,
                        modules,
                        line_index
                    )

                    print(
                        random.randint(
                            int(first),
                            int(second)
                        )
                    )

            line_index += 1
            continue

        # ----------------------------------------------------
        # MATH
        # ----------------------------------------------------

        if (
            line.startswith("add(")
            and line.endswith(")")
        ):

            if not state["math"]:

                errors.handle(
                    line_index,
                    "Math module not found, try using `get math`"
                )

            else:

                values = split_arguments(
                    line[4:-1]
                )

                if len(values) != 2:

                    errors.handle(
                        line_index,
                        "add() requires 2 arguments."
                    )

                else:

                    left = resolve_value(
                        values[0],
                        variables,
                        modules,
                        line_index
                    )

                    right = resolve_value(
                        values[1],
                        variables,
                        modules,
                        line_index
                    )

                    print(
                        left + right
                    )

            line_index += 1
            continue

        if (
            line.startswith("subtract(")
            and line.endswith(")")
        ):

            if not state["math"]:

                errors.handle(
                    line_index,
                    "Math module not found, try using `get math`"
                )

            else:

                values = split_arguments(
                    line[9:-1]
                )

                if len(values) != 2:

                    errors.handle(
                        line_index,
                        "subtract() requires 2 arguments."
                    )

                else:

                    left = resolve_value(
                        values[0],
                        variables,
                        modules,
                        line_index
                    )

                    right = resolve_value(
                        values[1],
                        variables,
                        modules,
                        line_index
                    )

                    print(
                        left - right
                    )

            line_index += 1
            continue

        if (
            line.startswith("multiply(")
            and line.endswith(")")
        ):

            if not state["math"]:

                errors.handle(
                    line_index,
                    "Math module not found, try using `get math`"
                )

            else:

                values = split_arguments(
                    line[9:-1]
                )

                if len(values) != 2:

                    errors.handle(
                        line_index,
                        "multiply() requires 2 arguments."
                    )

                else:

                    left = resolve_value(
                        values[0],
                        variables,
                        modules,
                        line_index
                    )

                    right = resolve_value(
                        values[1],
                        variables,
                        modules,
                        line_index
                    )

                    print(
                        left * right
                    )

            line_index += 1
            continue

        if (
            line.startswith("divide(")
            and line.endswith(")")
        ):

            if not state["math"]:

                errors.handle(
                    line_index,
                    "Math module not found, try using `get math`"
                )

            else:

                values = split_arguments(
                    line[7:-1]
                )

                if len(values) != 2:

                    errors.handle(
                        line_index,
                        "divide() requires 2 arguments."
                    )

                else:

                    left = resolve_value(
                        values[0],
                        variables,
                        modules,
                        line_index
                    )

                    right = resolve_value(
                        values[1],
                        variables,
                        modules,
                        line_index
                    )

                    if right == 0:

                        errors.handle(
                            line_index,
                            "Cannot divide by 0"
                        )

                    else:

                        print(
                            left / right
                        )

            line_index += 1
            continue

        # ----------------------------------------------------
        # DISCORD: INTENTS
        # ----------------------------------------------------

        if (
            line.startswith("client.intents(")
            and line.endswith(")")
        ):

            if not state["discord"]:

                errors.handle(
                    line_index,
                    "Discord module not found, try using `get discord`"
                )

            else:

                values = split_arguments(
                    line[15:-1],
                    ";"
                )

                intent_names = []

                for value in values:

                    resolved = resolve_value(
                        value,
                        variables,
                        modules,
                        line_index
                    )

                    intent_names.append(
                        str(resolved)
                    )

                disc.setIntents(
                    *intent_names
                )

            line_index += 1
            continue

        # ----------------------------------------------------
        # DISCORD: RUN
        # ----------------------------------------------------

        if (
            line.startswith("client.run(")
            and line.endswith(")")
        ):

            if not state["discord"]:

                errors.handle(
                    line_index,
                    "Discord module not found, try using `get discord`"
                )

            else:

                token = resolve_value(
                    line[11:-1],
                    variables,
                    modules,
                    line_index
                )

                disc.handle(
                    str(token)
                )

            line_index += 1
            continue

        # ----------------------------------------------------
        # DISCORD: COMMAND
        # ----------------------------------------------------

        if (
            line.startswith("client.command(")
            and line.endswith(")")
        ):

            if not state["discord"]:

                errors.handle(
                    line_index,
                    "Discord module not found, try using `get discord`"
                )

            else:

                values = split_arguments(
                    line[15:-1],
                    ";"
                )

                if len(values) != 2:

                    errors.handle(
                        line_index,
                        "client.command() requires a name and message."
                    )

                else:

                    command_name = resolve_value(
                        values[0],
                        variables,
                        modules,
                        line_index
                    )

                    message = resolve_value(
                        values[1],
                        variables,
                        modules,
                        line_index
                    )

                    disc.clientCommand(
                        str(command_name),
                        str(message)
                    )

            line_index += 1
            continue

        # ----------------------------------------------------
        # DISCORD: SLASH
        # ----------------------------------------------------

        if (
            line.startswith("client.slash(")
            and line.endswith(")")
        ):

            if not state["discord"]:

                errors.handle(
                    line_index,
                    "Discord module not found, try using `get discord`"
                )

            else:

                values = split_arguments(
                    line[13:-1],
                    ";"
                )

                if len(values) != 3:

                    errors.handle(
                        line_index,
                        "client.slash() requires a name, description and message."
                    )

                else:

                    slash_name = resolve_value(
                        values[0],
                        variables,
                        modules,
                        line_index
                    )

                    description = resolve_value(
                        values[1],
                        variables,
                        modules,
                        line_index
                    )

                    message = resolve_value(
                        values[2],
                        variables,
                        modules,
                        line_index
                    )

                    disc.applicationCommand(
                        str(slash_name),
                        str(description),
                        str(message)
                    )

            line_index += 1
            continue

        # ----------------------------------------------------
        # DISCORD: SYNC
        # ----------------------------------------------------

        if line == "client.sync()":

            if not state["discord"]:

                errors.handle(
                    line_index,
                    "Discord module not found, try using `get discord`"
                )

            else:

                disc.sync()

            line_index += 1
            continue

        # ----------------------------------------------------
        # DISCORD: EVENT
        # ----------------------------------------------------

        if (
            line.startswith("client.event(")
            and line.endswith(")")
        ):

            if not state["discord"]:

                errors.handle(
                    line_index,
                    "Discord module not found, try using `get discord`"
                )

            else:

                values = split_arguments(
                    line[13:-1],
                    ";"
                )

                if len(values) != 3:

                    errors.handle(
                        line_index,
                        "client.event() requires an event, channel and message."
                    )

                else:

                    event_name = resolve_value(
                        values[0],
                        variables,
                        modules,
                        line_index
                    )

                    channel = resolve_value(
                        values[1],
                        variables,
                        modules,
                        line_index
                    )

                    message = resolve_value(
                        values[2],
                        variables,
                        modules,
                        line_index
                    )

                    disc.event(
                        str(event_name),
                        str(channel),
                        str(message)
                    )

            line_index += 1
            continue

        # ----------------------------------------------------
        # RUN EXTERNAL PROGRAM
        # ----------------------------------------------------

        if (
            line.startswith("run(")
            and line.endswith(")")
        ):

            content = line[
                4:-1
            ].strip()

            parts = split_arguments(
                content,
                " "
            )

            if not parts:

                errors.handle(
                    line_index,
                    "run() requires a program."
                )

            else:

                program = resolve_value(
                    parts[0],
                    variables,
                    modules,
                    line_index
                )

                args = []

                for argument in parts[1:]:

                    args.append(
                        str(
                            resolve_value(
                                argument,
                                variables,
                                modules,
                                line_index
                            )
                        )
                    )

                try:

                    subprocess.run(
                        [str(program)] + args,
                        check=True
                    )

                except FileNotFoundError:

                    errors.handle(
                        line_index,
                        f"Program '{program}' not found."
                    )

                except subprocess.CalledProcessError as e:

                    errors.handle(
                        line_index,
                        f"Program exited with code {e.returncode}."
                    )

            line_index += 1
            continue

        # ----------------------------------------------------
        # FUNCTION / MODULE CALL
        # ----------------------------------------------------

        if (
            "(" in line
            and line.endswith(")")
        ):

            open_paren = line.find("(")

            name = line[
                :open_paren
            ].strip()

            args = line[
                open_paren + 1:-1
            ].strip()

            # ------------------------------------------------
            # MODULE FUNCTION
            # ------------------------------------------------

            if "." in name:

                result, handled = evaluate_method(
                    line,
                    variables,
                    modules,
                    line_index
                )

                if not handled:

                    errors.handle(
                        line_index,
                        f"Invalid module function call."
                    )

                elif result is not None:

                    return_value = result

            # ------------------------------------------------
            # NORMAL FUNCTION
            # ------------------------------------------------

            elif name in functionss:

                result = call_function(
                    functionss[name],
                    args,
                    variables,
                    modules,
                    functionss,
                    line_index
                )

                if isinstance(
                    result,
                    dict
                ) and result.get(
                    "return"
                ):

                    return result

                if result is not None:

                    return_value = result

            else:

                errors.handle(
                    line_index,
                    f"Function {name} not found."
                )

            line_index += 1
            continue

        # ----------------------------------------------------
        # UNKNOWN
        # ----------------------------------------------------

        errors.handle(
            line_index,
            "Unknown command!"
        )

        line_index += 1

    # --------------------------------------------------------
    # CLOSE OPEN FILE
    # --------------------------------------------------------

    file = state.get(
        "file"
    )

    if file is not None:

        try:

            file.close()

        except Exception:

            pass

        state[
            "file"
        ] = None

    return return_value
>>>>>>> 285454a (trust)
