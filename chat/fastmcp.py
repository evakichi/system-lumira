from fastmcp import FastMCP, Context
import requests
import os
import json

mcp = FastMCP(
        name="HTTP Calculator",
        instructions="""
        演算をします。
        """
        )

@mcp.tool()
def add(a: float, b: float) -> float:
    """二つの数値を足し算します"""
    return a + b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """二つの数値を掛け算します"""
    return a * b

@mcp.tool()
def calculate_power(base: float, exponent: float) -> float:
    """べき乗を計算します（base の exponent 乗）"""
    return base ** exponent

if __name__ == "__main__":
    print("🌐 HTTP MCP Server starting...")
    print("📡 Endpoint: http://localhost:8000/mcp")
    print("🔧 Tools: add, multiply, calculate_power")
    
    # HTTP Transportで起動
    mcp.run(
        transport="http",
        host="0.0.0.0", 
        port=8000,
        path="/mcp"
    )
