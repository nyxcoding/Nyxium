def handle(line, message):
    PURPLE = "\033[35m"
    RESET = "\033[0m"
    print(f"{PURPLE}Nyxium line {line}: {message}{RESET}")