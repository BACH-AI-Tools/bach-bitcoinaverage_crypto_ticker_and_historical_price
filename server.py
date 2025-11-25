"""
Bitcoinaverage Crypto Ticker And Historical Price MCP Server

使用 FastMCP 的 from_openapi 方法自动生成

Version: 1.0.0
Transport: stdio
"""
import os
import json
import httpx
from fastmcp import FastMCP

# 服务器版本和配置
__version__ = "1.0.0"
__tag__ = "bitcoinaverage_crypto_ticker_and_historical_price/1.0.0"

# API 配置
API_KEY = os.getenv("API_KEY", "")

# 传输协议配置
TRANSPORT = "stdio"


# OpenAPI 规范
OPENAPI_SPEC = """{\n  \"openapi\": \"3.0.0\",\n  \"info\": {\n    \"title\": \"Bitcoinaverage Crypto Ticker And Historical Price\",\n    \"version\": \"1.0.0\",\n    \"description\": \"RapidAPI: blockchain-data-ltd-blockchain-data-ltd-default/bitcoinaverage-crypto-ticker-and-historical-price\"\n  },\n  \"servers\": [\n    {\n      \"url\": \"https://bitcoinaverage-crypto-ticker-and-historical-price.p.rapidapi.com\"\n    }\n  ],\n  \"paths\": {\n    \"/exchanges/ticker/{exchange}\": {\n      \"get\": {\n        \"summary\": \"Crypto Exchange Ticker price\",\n        \"description\": \"Get the latest price data for specific cryptocurrency exchange.\",\n        \"operationId\": \"crypto_exchange_ticker_price\",\n        \"parameters\": [\n          {\n            \"name\": \"exchange\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: bitstamp\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/indices/{symbol_set}/history/{symbol}\": {\n      \"get\": {\n        \"summary\": \"Historical price data for period\",\n        \"description\": \"Returns history price for specific symbol for certain period. Works in parallel to the Ticker endpoint where both symbol set and market symbol need to be specified. This endpoint additionally accepts the period query parameter that specifies the resolution of the data. Period can be: minute, hour or day.\",\n        \"operationId\": \"historical_price_data_for_period\",\n        \"parameters\": [\n          {\n            \"name\": \"period\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: day\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"symbol_set\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: global\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"symbol\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: BTCUSD\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/indices/{symbol_set}/ticker/{symbol}\": {\n      \"get\": {\n        \"summary\": \"Cryptocurrency Index Ticker price\",\n        \"description\": \"Get the latest Ticker price for thousands of cryptocurrencies. Our Ticker data includes the latest price, bid, ask, 24h volume, moving average and price changes.\",\n        \"operationId\": \"cryptocurrency_index_ticker_price\",\n        \"parameters\": [\n          {\n            \"name\": \"symbol_set\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Symbol set can be one of: global, local, crypto, tokens and light\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"symbol\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"The shorthand symbol of the market you are requesting data for. A full list of supported symbols grouped by symbol set can be found here.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/info/indices/ticker\": {\n      \"get\": {\n        \"summary\": \"List of all supported crypto markets\",\n        \"description\": \"Lists all supported cryptocurrency markets by the BitcoinAverage API. New cryptos or tokens are added on a monthly basis.\",\n        \"operationId\": \"list_of_all_supported_crypto_markets\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    }\n  },\n  \"components\": {\n    \"securitySchemes\": {\n      \"ApiAuth\": {\n        \"type\": \"apiKey\",\n        \"in\": \"header\",\n        \"name\": \"X-RapidAPI-Key\"\n      }\n    }\n  },\n  \"security\": [\n    {\n      \"ApiAuth\": []\n    }\n  ]\n}"""

# 创建 HTTP 客户端
# 设置默认 headers
default_headers = {}


# RapidAPI 必需的 headers
if API_KEY:
    default_headers["X-RapidAPI-Key"] = API_KEY
    default_headers["X-RapidAPI-Host"] = "bitcoinaverage-crypto-ticker-and-historical-price.p.rapidapi.com"
else:
    print("⚠️  警告: 未设置 API_KEY 环境变量")
    print("   RapidAPI 需要 API Key 才能正常工作")
    print("   请设置: export API_KEY=你的RapidAPI-Key")

# 对于 POST/PUT/PATCH 请求，自动添加 Content-Type
default_headers["Content-Type"] = "application/json"




client = httpx.AsyncClient(
    base_url="https://bitcoinaverage-crypto-ticker-and-historical-price.p.rapidapi.com", 
    timeout=30.0
)


# 从 OpenAPI 规范创建 FastMCP 服务器
openapi_dict = json.loads(OPENAPI_SPEC)
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_dict,
    client=client,
    name="bitcoinaverage_crypto_ticker_and_historical_price",
    version=__version__
)


# 注册请求拦截器，为所有请求添加 RapidAPI headers
_original_request = client.request

async def _add_rapidapi_headers(method, url, **kwargs):
    """拦截所有请求，添加必需的 RapidAPI headers"""
    # 确保 headers 存在
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    
    # 添加 RapidAPI 必需的 headers
    if API_KEY:
        kwargs['headers']['X-RapidAPI-Key'] = API_KEY
        kwargs['headers']['X-RapidAPI-Host'] = "bitcoinaverage-crypto-ticker-and-historical-price.p.rapidapi.com"
    else:
        print("⚠️  警告: API_KEY 未设置，请求可能失败")
    
    # 对于 POST/PUT/PATCH，添加 Content-Type
    if method.upper() in ['POST', 'PUT', 'PATCH']:
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
    
    return await _original_request(method, url, **kwargs)

# 替换 request 方法
client.request = _add_rapidapi_headers


def main():
    """主入口点"""
    print(f"🚀 启动 Bitcoinaverage Crypto Ticker And Historical Price MCP 服务器")
    print(f"📦 版本: {__tag__}")
    print(f"🔧 传输协议: {TRANSPORT}")
    
    print()
    
    # 运行服务器
    
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()