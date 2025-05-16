from phi.assistant import Assistant
from phi.llm import LLM
from phi.tools.yfinance import YFinanceTools
import os

assistant = Assistant(
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,company_info=True,company_news=True)],
    llm=LLM(model="gpt-4o", temperature=0, max_tokens=2000,api_key=os.getenv("OPENAI_API_KEY")),
    show_tool_calls=True,
    markdown=True
)

assistant.print_response("What is the stock price of Apple and Amazon")
assistant.print_response("Write a comparison between Apple and Amazon, use all tools available.")

