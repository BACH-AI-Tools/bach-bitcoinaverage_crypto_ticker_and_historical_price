# Bitcoinaverage Crypto Ticker And Historical Price MCP Server

[English](./README_EN.md) | 简体中文 | [繁體中文](./README_ZH-TW.md)

## 🚀 使用 EMCP 平台快速体验

**[EMCP](https://sit-emcp.kaleido.guru)** 是一个强大的 MCP 服务器管理平台，让您无需手动配置即可快速使用各种 MCP 服务器！

### 快速开始：

1. 🌐 访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 注册并登录账号
3. 🎯 进入 **MCP 广场**，浏览所有可用的 MCP 服务器
4. 🔍 搜索或找到本服务器（`bach-bitcoinaverage_crypto_ticker_and_historical_price`）
5. 🎉 点击 **"安装 MCP"** 按钮
6. ✅ 完成！即可在您的应用中使用

### EMCP 平台优势：

- ✨ **零配置**：无需手动编辑配置文件
- 🎨 **可视化管理**：图形界面轻松管理所有 MCP 服务器
- 🔐 **安全可靠**：统一管理 API 密钥和认证信息
- 🚀 **一键安装**：MCP 广场提供丰富的服务器选择
- 📊 **使用统计**：实时查看服务调用情况

立即访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 开始您的 MCP 之旅！


---

## 简介

这是一个 MCP 服务器，用于访问 Bitcoinaverage Crypto Ticker And Historical Price API。

- **PyPI 包名**: `bach-bitcoinaverage_crypto_ticker_and_historical_price`
- **版本**: 2.0.0
- **传输协议**: stdio


## 安装

### 从 PyPI 安装:

```bash
pip install bach-bitcoinaverage_crypto_ticker_and_historical_price
```

### 从源码安装:

```bash
pip install -e .
```

## 运行

### 方式 1: 使用 uvx（推荐，无需安装）

```bash
# 运行（uvx 会自动安装并运行）
uvx --from bach-bitcoinaverage_crypto_ticker_and_historical_price bach_bitcoinaverage_crypto_ticker_and_historical_price

# 或指定版本
uvx --from bach-bitcoinaverage_crypto_ticker_and_historical_price@latest bach_bitcoinaverage_crypto_ticker_and_historical_price
```

### 方式 2: 直接运行（开发模式）

```bash
python server.py
```

### 方式 3: 安装后作为命令运行

```bash
# 安装
pip install bach-bitcoinaverage_crypto_ticker_and_historical_price

# 运行（命令名使用下划线）
bach_bitcoinaverage_crypto_ticker_and_historical_price
```

## 配置

### API 认证

此 API 需要认证。请设置环境变量:

```bash
export API_KEY="your_api_key_here"
```

### 环境变量

| 变量名 | 说明 | 必需 |
|--------|------|------|
| `API_KEY` | API 密钥 | 是 |
| `PORT` | 不适用 | 否 |
| `HOST` | 不适用 | 否 |



### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "bitcoinaverage_crypto_ticker_and_historical_price": {
      "command": "uvx",
      "args": ["--from", "bach-bitcoinaverage_crypto_ticker_and_historical_price", "bach_bitcoinaverage_crypto_ticker_and_historical_price"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**注意**: 请将 `E:\path\to\bitcoinaverage_crypto_ticker_and_historical_price\server.py` 替换为实际的服务器文件路径。


## 可用工具

此服务器提供以下工具:


### `crypto_exchange_ticker_price`

Get the latest price data for specific cryptocurrency exchange.

**端点**: `GET /exchanges/ticker/{exchange}`


**参数**:

- `exchange` (string) *必需*: Example value: bitstamp



---


### `historical_price_data_for_period`

Returns history price for specific symbol for certain period. Works in parallel to the Ticker endpoint where both symbol set and market symbol need to be specified. This endpoint additionally accepts the period query parameter that specifies the resolution of the data. Period can be: minute, hour or day.

**端点**: `GET /indices/{symbol_set}/history/{symbol}`


**参数**:

- `period` (string): Example value: day

- `symbol_set` (string) *必需*: Example value: global

- `symbol` (string) *必需*: Example value: BTCUSD



---


### `cryptocurrency_index_ticker_price`

Get the latest Ticker price for thousands of cryptocurrencies. Our Ticker data includes the latest price, bid, ask, 24h volume, moving average and price changes.

**端点**: `GET /indices/{symbol_set}/ticker/{symbol}`


**参数**:

- `symbol_set` (string) *必需*: Symbol set can be one of: global, local, crypto, tokens and light

- `symbol` (string) *必需*: The shorthand symbol of the market you are requesting data for. A full list of supported symbols grouped by symbol set can be found here.



---


### `list_of_all_supported_crypto_markets`

Lists all supported cryptocurrency markets by the BitcoinAverage API. New cryptos or tokens are added on a monthly basis.

**端点**: `GET /info/indices/ticker`



---



## 技术栈

- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

此服务器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自动生成。

版本: 2.0.0
