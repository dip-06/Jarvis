from brain.groq_brain import ask_groq
from brain.dispatcher import execute_tool_calls
message = ask_groq("close file exploorer")
print(message)
if message.tool_calls:
    execute_tool_calls(message)
# from Desktop_application_control.closeapp import set_focus
# set_focus("focus brave")