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
                ints = line(8: -1).split()
                
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
        
        elif line.endswith("()")
            name = line[:-2]
            if name in functionss:
                run("\n".join(functionss[name]))
            else:
                errors.handle(line_index, f"Function {name} not found.")
                
        else:
            print(f"Unknown command: Line {line_index + 1}")
        
        line_index += 1
