`return f"HTTP/1.1 {code} OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n{content}"`

###

User-Agent Syntax

User-Agent: <product> / <product-version> <comment>

Common format for web browsers:

User-Agent: Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>

---

Use match for paths/errors?

> A match statement takes an expression and compares its value to successive patterns given as one or more case blocks. This is superficially similar to a
> switch statement in C, Java or JavaScript (and many other languages), but it’s more similar to pattern matching in languages like Rust or Haskell.
> Only the first pattern that matches gets executed and it can also extract components (sequence elements or object attributes) from the value into variables.

```python
# 4.6. match Statements
# The simplest form compares a subject value against one or more literals:

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# Note the last block: the “variable name” _ acts as a wildcard and never fails to match. If no case matches, none of the branches is executed.

# You can combine several literals in a single pattern using | (“or”):

case 401 | 403 | 404:
    return "Not allowed"

# Patterns can look like unpacking assignments, and can be used to bind variables:

# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

# Study that one carefully! The first pattern has two literals, and can be thought of as an extension of the literal pattern shown above. But the next two patterns combine a literal and a variable, and the # variable binds a value from the subject (point). The fourth pattern captures two values, which makes it conceptually similar to the unpacking assignment (x, y) = point.
```

---

if line.startswith("User-Agent:"):
user_agent = line.split(" ")[1]

```python

# Gather all of the responses
response_body = f"{str_result}".encode("utf-8")
status_line = b"HTTP/1.1 200 OK\r\n"
content_type = b"Content-Type: text/plain\r\n"
content_length = f"Content-Length: {len(response_body)}\r\n".encode("utf-8")

# Create the header response
response_headers = content_type + content_length
response = status_line + response_headers + b"\r\n" + response_body
# return f"HTTP/1.1 {code} OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n{content}"

# return response
return response
```

---
