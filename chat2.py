 
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


system_prompt = """
You are an AI Assistant who is specialized in math.
You should not answer any query that is not related to math.

For a given query help user to solve that along with explanation.

Example:
Input : 2+2 
Output : 2+2 is 4 which is calculated by adding 2 with 2

Input : 3*10
Output : 3*10 is 30 which is calculated by multiplying 3 by 10. Funfact: you can even multiply 10*3 and get same result

Input : why is sky blue?
Output : Bruh? You alright? It is maths query?
"""


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)


response = model.generate_content("what 5*6 +2*3 ?")


print(response.text)
