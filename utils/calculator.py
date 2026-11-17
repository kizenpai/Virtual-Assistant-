"""
Safe Mathematical Calculator for NOVA.

Evaluates mathematical expressions using Abstract Syntax Trees (AST)
without executing arbitrary code or using unsafe `eval()`.
Includes natural language query parsing.
"""

import ast
import math
import operator
import re
from typing import Any, Union

# Supported binary operators
SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

# Supported unary operators
SAFE_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

# Allowed mathematical functions and constants
SAFE_FUNCTIONS = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "abs": abs,
    "round": round,
    "floor": math.floor,
    "ceil": math.ceil,
}

SAFE_CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}

class SafeEvaluator:
    """Safely evaluates AST nodes for arithmetic operations."""

    def evaluate(self, node: ast.AST) -> Union[int, float]:
        if isinstance(node, ast.Expression):
            return self.evaluate(node.body)

        elif isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError(f"Unsupported constant type: {type(node.value)}")


        elif isinstance(node, ast.Name):
            name_lower = node.id.lower()
            if name_lower in SAFE_CONSTANTS:
                return SAFE_CONSTANTS[name_lower]
            raise ValueError(f"Undefined variable or constant: '{node.id}'")

        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in SAFE_OPERATORS:
                raise ValueError(f"Unsupported operator: {op_type.__name__}")
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            # Prevent excessive exponentiation denial-of-service
            if op_type is ast.Pow:
                if abs(right) > 1000 or abs(left) > 10000:
                    raise OverflowError("Exponentiation values are too large.")

            func = SAFE_OPERATORS[op_type]
            return func(left, right)

        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in SAFE_UNARY_OPERATORS:
                raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
            operand = self.evaluate(node.operand)
            return SAFE_UNARY_OPERATORS[op_type](operand)

        elif isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Nested or attribute function calls are not allowed.")
            func_name = node.func.id.lower()
            if func_name not in SAFE_FUNCTIONS:
                raise ValueError(f"Function '{func_name}' is not supported.")
            args = [self.evaluate(arg) for arg in node.args]
            return SAFE_FUNCTIONS[func_name](*args)

        else:
            raise ValueError(f"Unsupported expression syntax: {type(node).__name__}")


def extract_math_expression(text: str) -> str:
    """
    Extracts and normalizes arithmetic phrases from conversational input.
    Examples:
      'what is 5 plus 5' -> '5 + 5'
      'calculate 10 times 20' -> '10 * 20'
      'how much is 100 divided by 4' -> '100 / 4'
      'solve 2 power 3' -> '2 ** 3'
    """
    clean = text.lower().strip()

    # Strip conversational prefixes
    prefixes = [
        r"^(calculate|compute|solve|evaluate)\s+",
        r"^(what is|what's|how much is)\s+",
        r"^(can you calculate|please calculate)\s+",
        r"^math\s+",
    ]
    for p in prefixes:
        clean = re.sub(p, "", clean, flags=re.IGNORECASE)

    # Word substitutions
    substitutions = [
        (r"\bplus\b", "+"),
        (r"\bminus\b", "-"),
        (r"\btimes\b", "*"),
        (r"\bmultiplied\s+by\b", "*"),
        (r"\binto\b", "*"),
        (r"\bx\b", "*"),
        (r"\bdivided\s+by\b", "/"),
        (r"\bdivide\s+by\b", "/"),
        (r"\bover\b", "/"),
        (r"\bmodulo\b", "%"),
        (r"\bmod\b", "%"),
        (r"\bto\s+the\s+power\s+of\b", "**"),
        (r"\bpower\s+of\b", "**"),
        (r"\bpower\b", "**"),
        (r"\braised\s+to\b", "**"),
        (r"\^", "**"),
        (r"\bsquare\s+root\s+of\s+([0-9.]+)", r"sqrt(\1)"),
    ]
    for pattern, repl in substitutions:
        clean = re.sub(pattern, repl, clean, flags=re.IGNORECASE)

    # Remove trailing question marks or punctuation
    clean = re.sub(r"[?!;,]+$", "", clean).strip()
    return clean


def calculate(expression_or_text: str) -> str:
    """
    Safely calculates the result of a mathematical expression or query.

    Returns:
        Formatted string representing the calculation and answer.
    """
    expr = extract_math_expression(expression_or_text)
    if not expr:
        return "Please provide a valid mathematical expression."

    try:
        parsed = ast.parse(expr, mode="eval")
        evaluator = SafeEvaluator()
        result = evaluator.evaluate(parsed)

        # Pretty formatting: avoid 5.0 for integer results
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        elif isinstance(result, float):
            result = round(result, 6)

        return f"The result of {expr} is {result}"

    except ZeroDivisionError:
        return "Cannot divide by zero."
    except OverflowError:
        return "Calculation error: Number is too large to compute."
    except ValueError as ve:
        return f"Calculation error: {ve}"
    except SyntaxError:
        return f"Could not parse mathematical expression '{expr}'. Please check the format."
    except Exception as e:
        return f"Unable to calculate expression: {e}"
