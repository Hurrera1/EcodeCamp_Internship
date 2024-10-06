import gradio as gr
import math

# Simple Calculator
def simple_calculator(num1, operator, num2):
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
        else:
            return "Error: Invalid operator"
    except Exception as e:
        return str(e)

# Advanced Calculator
def advanced_calculator(num1, operator, num2):
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
        elif operator == "^":
            return num1 ** num2
        elif operator == "sin":
            return math.sin(math.radians(num1))
        elif operator == "cos":
            return math.cos(math.radians(num1))
        elif operator == "tan":
            return math.tan(math.radians(num1))
        elif operator == "sqrt":
            if num1 >= 0:
                return math.sqrt(num1)
            else:
                return "Error: Square root of negative number"
        elif operator == "log":
            if num1 > 0:
                return math.log(num1)
            else:
                return "Error: Logarithm of non-positive number"
        else:
            return "Error: Invalid operator"
    except Exception as e:
        return str(e)


# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Calculator")
    with gr.Tab("Simple Calculator"):
        gr.Markdown("### Simple Calculator")
        gr.Markdown("This calculator performs basic arithmetic operations.")
        num1 = gr.Number(label="Number 1")
        operator = gr.Radio(["+", "-", "*", "/"], label="Operator")
        num2 = gr.Number(label="Number 2")
        result = gr.Number(label="Result")
        gr.Button("Calculate").click(simple_calculator, inputs=[num1, operator, num2], outputs=result)
    
    with gr.Tab("Advanced Calculator"):
        gr.Markdown("### Advanced Calculator")
        gr.Markdown("This calculator performs advanced arithmetic operations, including exponentiation, trigonometric functions, and logarithms.")
        num1 = gr.Number(label="Number 1")
        operator = gr.Radio([ "^", "sin", "cos", "tan", "sqrt", "log"], label="Operator")
        num2 = gr.Number(label="Number 2")
        result = gr.Number(label="Result")
        gr.Button("Calculate").click(advanced_calculator, inputs=[num1, operator, num2], outputs=result)

demo.launch()