from mcp.server.fastmcp import FastMCP
mcp=FastMCP("Math")
@mcp.tool()
def add(a:int, b:int)->int:
    """summary
    Add two numbers"""
    return a+b

@mcp.tool()
def multiply(a:int,b:int)->int:
    """multply two numbers
    """
    return a*b


# transport = stdio -> use standard input/output (stdi.stdout) to recieve and respond to tool function calls

if __name__ == "__main__":
    mcp.run(transport="stdio")