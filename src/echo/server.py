import logging
from mcp.server.fastmcp import FastMCP
from fastapi.responses import JSONResponse, HTMLResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Starting application with DEBUG logging enabled")

mcp = FastMCP("echo", host="0.0.0.0", port=8080)

# This exposes three routes to a web service
# /sse
# /healthz - health check
# /messages


@mcp.custom_route("/healthz", methods=["GET"])
async def health_check(request):
    return JSONResponse({"status": "ok"})


@mcp.custom_route("/", methods=["GET"])
async def home_dir(request):
    # return a simple html page with a link to the sse endpoint
    return HTMLResponse(content="<h1>Hello , I'm working well</h1>")


@mcp.resource("echo://{message}")
async def echo_resource(message: str) -> str:
    """Echo a message as a resource"""
    return f"Resource echo: {message}"


@mcp.tool()
async def echo_tool(message: str) -> str:
    """Echo a message as a tool"""
    return f"Tool echo: {message}"


@mcp.prompt("system_prompt")
async def system_prompt() -> str:
    """Defines the system prompt for the agent"""
    return f"You are a Agent that is specialized in repeating whatever the user says. For example, if the user says 'Hello', you should say 'Hello'."


@mcp.prompt("test_prompt")
async def echo_prompt(message: str) -> str:
    """Create an echo prompt"""
    return f"Please process this message: {message}"


@mcp.tool("get_weather", "This tool gets the current temperature in a city.")
async def get_weather(city_name: str) -> int:
    """
    This tool gets the current temperature in a city.

    Args:
        city: str

    Returns:
        int: The temperature in the city
    """
    import random
    return 22  # random.randint(4, 30)

# mcp.run('sse')
