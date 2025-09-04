from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
from langchain_core.tools import tool


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""

    return a * b


print(multiply.args_schema.model_json_schema())  # LLM Sees this
# {
#     "description": "Multiply two numbers",
#     "properties": {
#         "a": {"title": "A", "type": "integer"},
#         "b": {"title": "B", "type": "integer"},
#     },
#     "required": ["a", "b"],
#     "title": "multiply",
#     "type": "object",
# }


# Another Method of Creating Tool


class SummerInput(BaseModel):
    num1: float = Field(required=True, description="First number to add.")
    num2: float = Field(required=True, description="Second number to add.")


def summer(num1: int, num2: int) -> int:
    return num1 + num2


sum_tool = StructuredTool.from_function(
    func=summer, name="summer", description="Add two numbers", args_schema=SummerInput
)

result = sum_tool.invoke({"num1": 3, "num2": 5})

print(sum_tool.args_schema.model_json_schema())  # LLM Sees this
# {
#     "properties": {
#         "num1": {
#             "description": "First number to add.",
#             "required": True,
#             "title": "Num1",
#             "type": "number",
#         },
#         "num2": {
#             "description": "Second number to add.",
#             "required": True,
#             "title": "Num2",
#             "type": "number",
#         },
#     },
#     "required": ["num1", "num2"],
#     "title": "SummerInput",
#     "type": "object",
# }

print(result)


# Creating a Toolkit


class MathToolkit:
    def get_tools(self):
        return [multiply, sum_tool]


toolkit = MathToolkit()

tools = toolkit.get_tools()

for tol in tools:
    print(tol.name)
