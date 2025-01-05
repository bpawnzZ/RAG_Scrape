# https://github.com/ccxt/ccxt#start-of-content

Skip to content
Navigation Menu
Sign in
ccxt
/
ccxt
Public
 Sponsor
Notifications
Fork 7.6k
 Star 33.9k
Code
Issues
859
Pull requests
456
Actions
Projects
21
Wiki
ccxt/ccxt
 master
Go to file
Code
Folders and files
Name	Last commit message	Last commit date

Latest commit
Travis CI
fix(binance): pm exception mapping (#24750)
d029b92
 · 
History


.git-templates/hooks
	
fix(template): return error code
	


.github
	
README / wiki ticker-structure doc links
	


build
	
detect missing parser methods (#24738)
	


cs
	
fix(binance): pm exception mapping (#24750)
	


dist
	
fix(binance): pm exception mapping (#24750)
	


doc
	
build(deps): bump readthedocs-sphinx-search from 0.1.0 to 0.3.2 in /d…
	


examples
	
build(deps): bump next from 14.2.15 to 14.2.21 in /examples/ts/nextjs…
	


js
	
fix(binance): pm exception mapping (#24750)
	


php
	
fix(binance): pm exception mapping (#24750)
	


python
	
fix(binance): pm exception mapping (#24750)
	


ts
	
fix(binance): pm exception mapping (#24750)
	


utils
	
fix(tests) - static updater (#24412)
	


wiki
	
4.4.45
	


.dockerignore
	
docker: update dockerignore file (#23281)
	


.eslintignore
	
add eslintignore
	


.gitattributes
	
fix images format [ci deploy] (#21088)
	


.gitignore
	
feat(dev): .gitignore - added .custom_gitignore (#23039)
	


.npmignore
	
fix(npm): browser bundle (#22566)
	


.travis.yml
	
fix future reject hanging error (#23161)
	


CHANGELOG.md
	
chore: update changelog (#24684)
	


CODEOWNERS
	
chore: update codeowners (#24137)
	


CONTRIBUTING.md
	
fix(php) - version numbers (#24641)
	


Dockerfile
	
tests: fix python tests in docker (#23213)
	


ISSUE_TEMPLATE.md
	
ISSUE_TEMPLATE.md #7486
	


LICENSE.txt
	
Update LICENSE.txt (#22366)
	


README.md
	
4.4.45
	


appveyor.yml
	
fix(appveyor): cinst replacement (#22738)
	


build.sh
	
tests(static) - detect & retest exchanges (#24670)
	


ccxt.php
	
chore: update auth method in upbit.ts file (#23492)
	


cleanup.sh
	
feat(sh): update cleanup (#24053)
	


coin-ws.js
	
mexc: update withdraw (#23065)
	


composer-install.sh
	
composer-install
	


composer.json
	
Merge branch 'master' into promise-interface-php
	


composer.lock
	
php promise v3 fixes
	


docker-compose.yml
	
update docker-compose.yml (fixed bug with php in docker) (#23172)
	


examples2md.js
	
minor edits
	


exchanges.cfg
	
minor edits
	


gource.sh
	
gource.sh visualisation
	


index.html
	
Updated GitHub URL
	


jsdoc2md.js
	
Disaster docs moving to get doc build broken (#24281)
	


keys.json
	
add sample exchange
	


package-lock.json
	
4.4.45
	


package.json
	
4.4.45
	


phpunit.xml.dist
	
PHP: Unit tests: init
	


postinstall.js
	
okx fetchMyTrades() ratelimit
	


pro-tests.json
	
Merge branch 'master' of github.com:ccxt/ccxt into poloniexfutures-so…
	


pyproject.toml
	
build: add Ruff (drop flake8)
	


rollup.config.js
	
feat(npmignore): rewrite npmignore (#22174)
	


run-tests.js
	
tests related fixes (#24389)
	


setup.cfg
	
added tox flake8 cd .. and python bitfinex example
	


skip-tests.json
	
tests(lykke) - try with proxy (#24724)
	


tests-manager.sh
	
chore: add freshness-test (#22327)
	


tsconfig.json
	
fix: ws memory leak on watchMultiple by using watchable un promise as…
	


webpack.config.js
	
minor edit to webpack config file
	
Repository files navigation
README
MIT license
CCXT – CryptoCurrency eXchange Trading Library

      

A JavaScript / Python / PHP / C# library for cryptocurrency trading and e-commerce with support for many bitcoin/ether/altcoin exchange markets and merchant APIs.

Install · Usage · Manual · FAQ · Examples · Contributing · Social

The CCXT library is used to connect and trade with cryptocurrency exchanges and payment processing services worldwide. It provides quick access to market data for storage, analysis, visualization, indicator development, algorithmic trading, strategy backtesting, bot programming, and related software engineering.

It is intended to be used by coders, developers, technically-skilled traders, data-scientists and financial analysts for building trading algorithms.

Current feature list:

support for many cryptocurrency exchanges — more coming soon
fully implemented public and private APIs
optional normalized data for cross-exchange analytics and arbitrage
an out of the box unified API that is extremely easy to integrate
works in Node 10.4+, Python 3, PHP 8.1+, netstandard2.0/2.1 and web browsers
Sponsored Promotion

See Also
 TabTrader – trading on all exchanges in one app. Available on Android and iOS!
 Freqtrade – leading opensource cryptocurrency algorithmic trading software!
 OctoBot – cryptocurrency trading bot with an advanced web interface.
 TokenBot – discover and copy the best algorithmic traders in the world.
Certified Cryptocurrency Exchanges
logo	id	name	ver	type	certified	pro	discount
	binance	Binance		cex			
	binancecoinm	Binance COIN-M		cex			
	binanceusdm	Binance USDⓈ-M		cex			
	bingx	BingX		cex			
	bitget	Bitget		cex			
	bitmart	BitMart		cex			
	bitmex	BitMEX		cex			
	bybit	Bybit		cex			
	coinbase	Coinbase Advanced		cex			
	coinbaseinternational	Coinbase International		cex			
	coinex	CoinEx		cex			
	cryptocom	Crypto.com		cex			
	gate	Gate.io		cex			
	hashkey	HashKey Global		cex			
	htx	HTX		cex			
	hyperliquid	Hyperliquid		dex			
	kucoin	KuCoin		cex			
	kucoinfutures	KuCoin Futures		cex			
	mexc	MEXC Global		cex			
	okx	OKX		cex			
	woo	WOO X		cex			
	woofipro	WOOFI PRO		dex			
Supported Cryptocurrency Exchanges

The CCXT library currently supports the following 107 cryptocurrency exchange markets and trading APIs:

logo	id	name	ver	type	certified	pro
	ace	ACE		cex		
	alpaca	Alpaca		cex		
	ascendex	AscendEX		cex		
	bequant	Bequant		cex		
	bigone	BigONE		cex		
	binance	Binance		cex		
	binancecoinm	Binance COIN-M		cex		
	binanceus	Binance US		cex		
	binanceusdm	Binance USDⓈ-M		cex		
	bingx	BingX		cex		
	bit2c	Bit2C		cex		
	bitbank	bitbank		cex		
	bitbns	Bitbns		cex		
	bitfinex	Bitfinex		cex		
	bitfinex1	Bitfinex		cex		
	bitflyer	bitFlyer		cex		
	bitget	Bitget		cex		
	bithumb	Bithumb		cex		
	bitmart	BitMart		cex		
	bitmex	BitMEX		cex		
	bitopro	BitoPro		cex		
	bitrue	Bitrue		cex		
	bitso	Bitso		cex		
	bitstamp	Bitstamp		cex		
	bitteam	BIT.TEAM		cex		
	bitvavo	Bitvavo		cex		
	bl3p	BL3P		cex		
	blockchaincom	Blockchain.com		cex		
	blofin	BloFin		cex		
	btcalpha	BTC-Alpha		cex		
	btcbox	BtcBox		cex		
	btcmarkets	BTC Markets		cex		
	btcturk	BTCTurk		cex		
	bybit	Bybit		cex		
	cex	CEX.IO		cex		
	coinbase	Coinbase Advanced		cex		
	coinbaseexchange	Coinbase Exchange		cex		
	coinbaseinternational	Coinbase International		cex		
	coincatch	CoinCatch		cex		
	coincheck	coincheck		cex		
	coinex	CoinEx		cex		
	coinlist	Coinlist		cex		
	coinmate	CoinMate		cex		
	coinmetro	Coinmetro		cex		
	coinone	CoinOne		cex		
	coinsph	Coins.ph		cex		
	coinspot	CoinSpot		cex		
	cryptocom	Crypto.com		cex		
	currencycom	Currency.com		cex		
	defx	Defx X		dex		
	delta	Delta Exchange		cex		
	deribit	Deribit		cex		
	digifinex	DigiFinex		cex		
	ellipx	Ellipx		cex		
	exmo	EXMO		cex		
	fmfwio	FMFW.io		cex		
	gate	Gate.io		cex		
	gemini	Gemini		cex		
	hashkey	HashKey Global		cex		
	hitbtc	HitBTC		cex		
	hollaex	HollaEx		cex		
	htx	HTX		cex		
	huobijp	Huobi Japan		cex		
	hyperliquid	Hyperliquid		dex		
	idex	IDEX		dex		
	independentreserve	Independent Reserve		cex		
	indodax	INDODAX		cex		
	kraken	Kraken		cex		
	krakenfutures	Kraken Futures		cex		
	kucoin	KuCoin		cex		
	kucoinfutures	KuCoin Futures		cex		
	kuna	Kuna		cex		
	latoken	Latoken		cex		
	lbank	LBank		cex		
	luno	luno		cex		
	lykke	Lykke		cex		
	mercado	Mercado Bitcoin		cex		
	mexc	MEXC Global		cex		
	myokx	MyOKX (EEA)		cex		
	ndax	NDAX		cex		
	novadax	NovaDAX		cex		
	oceanex	OceanEx		cex		
	okcoin	OKCoin		cex		
	okx	OKX		cex		
	onetrading	One Trading		cex		
	oxfun	OXFUN		cex		
	p2b	p2b		cex		
	paradex	Paradex		dex		
	paymium	Paymium		cex		
	phemex	Phemex		cex		
	poloniex	Poloniex		cex		
	poloniexfutures	Poloniex Futures		cex		
	probit	ProBit		cex		
	timex	TimeX		cex		
	tokocrypto	Tokocrypto		cex		
	tradeogre	tradeogre		cex		
	upbit	Upbit		cex		
	vertex	Vertex		dex		
	wavesexchange	Waves.Exchange		dex		
	wazirx	WazirX		cex		
	whitebit	WhiteBit		cex		
	woo	WOO X		cex		
	woofipro	WOOFI PRO		dex		
	xt	XT		cex		
	yobit	YoBit		cex		
	zaif	Zaif		cex		
	zonda	Zonda		cex		

The list above is updated frequently, new crypto markets, exchanges, bug fixes, and API endpoints are introduced on a regular basis. See the Manual for more details. If you can't find a cryptocurrency exchange in the list above and want it to be added, post a link to it by opening an issue here on GitHub or send us an email.

The library is under MIT license, that means it's absolutely free for any developer to build commercial and opensource software on top of it, but use it at your own risk with no warranties, as is.

Install

The easiest way to install the CCXT library is to use a package manager:

ccxt in NPM (JavaScript / Node v7.6+)
ccxt in PyPI (Python 3.7.0+)
ccxt in Packagist/Composer (PHP 8.1+)
ccxt in Nuget (netstandard 2.0)

This library is shipped as an all-in-one module implementation with minimalistic dependencies and requirements:

js/ in JavaScript
python/ in Python (generated from JS)
php/ in PHP (generated from JS)

You can also clone it into your project directory from ccxt GitHub repository:

git clone https://github.com/ccxt/ccxt.git  # including 1GB of commit history

# or

git clone https://github.com/ccxt/ccxt.git --depth 1  # avoid downloading 1GB of commit history
JavaScript (NPM)

JavaScript version of CCXT works in both Node and web browsers. Requires ES6 and async/await syntax support (Node 7.6.0+). When compiling with Webpack and Babel, make sure it is not excluded in your babel-loader config.

ccxt in NPM

npm install ccxt
//cjs
var ccxt = require ('ccxt')
console.log (ccxt.exchanges) // print all available exchanges
//esm
import {version, exchanges} from 'ccxt';
console.log(version, Object.keys(exchanges));
JavaScript (for use with the <script> tag):

All-in-one browser bundle (dependencies included), served from a CDN of your choice:

jsDelivr: https://cdn.jsdelivr.net/npm/ccxt@4.4.45/dist/ccxt.browser.min.js
unpkg: https://unpkg.com/ccxt@4.4.45/dist/ccxt.browser.min.js

CDNs are not updated in real-time and may have delays. Defaulting to the most recent version without specifying the version number is not recommended. Please, keep in mind that we are not responsible for the correct operation of those CDN servers.

<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/ccxt@4.4.45/dist/ccxt.browser.min.js"></script>

Creates a global ccxt object:

console.log (ccxt.exchanges) // print all available exchanges
Python

ccxt in PyPI

pip install ccxt
import ccxt
print(ccxt.exchanges) # print a list of all available exchange classes

The library supports concurrent asynchronous mode with asyncio and async/await in Python 3.7.0+

import ccxt.async_support as ccxt # link against the asynchronous version of ccxt
orjson support

CCXT also supports orjson for parsing JSON since it is much faster than the builtin library. This is especially important when using websockets because some exchanges return big messages that need to be parsed and dispatched as quickly as possible.

However, orjson is not enabled by default because it is not supported by every python interpreter. If you want to opt-in, you just need to install it (pip install orjson) on your local environment. CCXT will detect the installion and pick it up automatically.

PHP

ccxt in PHP with Packagist/Composer (PHP 8.1+)

It requires common PHP modules:

cURL
mbstring (using UTF-8 is highly recommended)
PCRE
iconv
gmp
include "ccxt.php";
var_dump (\ccxt\Exchange::$exchanges); // print a list of all available exchange classes

The library supports concurrent asynchronous mode using tools from ReactPHP in PHP 8.1+. Read the Manual for more details.

.net/C#

ccxt in C# with Nuget (netstandard 2.0 and netstandard 2.1)

using ccxt;
Console.WriteLine(ccxt.Exchanges) // check this later
Docker

You can get CCXT installed in a container along with all the supported languages and dependencies. This may be useful if you want to contribute to CCXT (e.g. run the build scripts and tests — please see the Contributing document for the details on that).

Using docker-compose (in the cloned CCXT repository):

docker-compose run --rm ccxt

You don't need the Docker image if you're not going to develop CCXT. If you just want to use CCXT – just install it as a regular package into your project.

Documentation

Read the Manual for more details.

Usage
Intro

The CCXT library consists of a public part and a private part. Anyone can use the public part immediately after installation. Public APIs provide unrestricted access to public information for all exchange markets without the need to register a user account or have an API key.

Public APIs include the following:

market data
instruments/trading pairs
price feeds (exchange rates)
order books
trade history
tickers
OHLC(V) for charting
other public endpoints

In order to trade with private APIs you need to obtain API keys from an exchange's website. It usually means signing up to the exchange and creating API keys for your account. Some exchanges require personal info or identification. Sometimes verification may be necessary as well. In this case you will need to register yourself, this library will not create accounts or API keys for you. Some exchanges expose API endpoints for registering an account, but most exchanges don't. You will have to sign up and create API keys on their websites.

Private APIs allow the following:

manage personal account info
query account balances
trade by making market and limit orders
deposit and withdraw fiat and crypto funds
query personal orders
get ledger history
transfer funds between accounts
use merchant services

This library implements full public and private REST and WebSocket APIs for all exchanges in TypeScript, JavaScript, PHP and Python.

The CCXT library supports both camelcase notation (preferred in TypeScript and JavaScript) and underscore notation (preferred in Python and PHP), therefore all methods can be called in either notation or coding style in any language.

// both of these notations work in JavaScript/Python/PHP
exchange.methodName ()  // camelcase pseudocode
exchange.method_name () // underscore pseudocode

Read the Manual for more details.

JavaScript

CCXT now supports ESM and CJS modules

CJS
// cjs example
'use strict';
const ccxt = require ('ccxt');

(async function () {
    let kraken    = new ccxt.kraken ()
    let bitfinex  = new ccxt.bitfinex ({ verbose: true })
    let huobipro  = new ccxt.huobipro ()
    let okcoinusd = new ccxt.okcoin ({
        apiKey: 'YOUR_PUBLIC_API_KEY',
        secret: 'YOUR_SECRET_PRIVATE_KEY',
    })

    const exchangeId = 'binance'
        , exchangeClass = ccxt[exchangeId]
        , exchange = new exchangeClass ({
            'apiKey': 'YOUR_API_KEY',
            'secret': 'YOUR_SECRET',
        })

    console.log (kraken.id,    await kraken.loadMarkets ())
    console.log (bitfinex.id,  await bitfinex.loadMarkets  ())
    console.log (huobipro.id,  await huobipro.loadMarkets ())

    console.log (kraken.id,    await kraken.fetchOrderBook (kraken.symbols[0]))
    console.log (bitfinex.id,  await bitfinex.fetchTicker ('BTC/USD'))
    console.log (huobipro.id,  await huobipro.fetchTrades ('ETH/USDT'))

    console.log (okcoinusd.id, await okcoinusd.fetchBalance ())

    // sell 1 BTC/USD for market price, sell a bitcoin for dollars immediately
    console.log (okcoinusd.id, await okcoinusd.createMarketSellOrder ('BTC/USD', 1))

    // buy 1 BTC/USD for $2500, you pay $2500 and receive ฿1 when the order is closed
    console.log (okcoinusd.id, await okcoinusd.createLimitBuyOrder ('BTC/USD', 1, 2500.00))

    // pass/redefine custom exchange-specific order params: type, amount, price or whatever
    // use a custom order type
    bitfinex.createLimitSellOrder ('BTC/USD', 1, 10, { 'type': 'trailing-stop' })

}) ();
ESM
//esm example
import {version, binance} from 'ccxt';

console.log(version);
const exchange = new binance();
const ticker = await exchange.fetchTicker('BTC/USDT');
console.log(ticker);
Python
# coding=utf-8

import ccxt

hitbtc   = ccxt.hitbtc({'verbose': True})
bitmex   = ccxt.bitmex()
huobipro = ccxt.huobipro()
exmo     = ccxt.exmo({
    'apiKey': 'YOUR_PUBLIC_API_KEY',
    'secret': 'YOUR_SECRET_PRIVATE_KEY',
})
kraken = ccxt.kraken({
    'apiKey': 'YOUR_PUBLIC_API_KEY',
    'secret': 'YOUR_SECRET_PRIVATE_KEY',
})

exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
})

hitbtc_markets = hitbtc.load_markets()

print(hitbtc.id, hitbtc_markets)
print(bitmex.id, bitmex.load_markets())
print(huobipro.id, huobipro.load_markets())

print(hitbtc.fetch_order_book(hitbtc.symbols[0]))
print(bitmex.fetch_ticker('BTC/USD'))
print(huobipro.fetch_trades('LTC/USDT'))

print(exmo.fetch_balance())

# sell one ฿ for market price and receive $ right now
print(exmo.id, exmo.create_market_sell_order('BTC/USD', 1))

# limit buy BTC/EUR, you pay €2500 and receive ฿1  when the order is closed
print(exmo.id, exmo.create_limit_buy_order('BTC/EUR', 1, 2500.00))

# pass/redefine custom exchange-specific order params: type, amount, price, flags, etc...
kraken.create_market_buy_order('BTC/USD', 1, {'trading_agreement': 'agree'})
PHP
include 'ccxt.php';

$poloniex = new \ccxt\poloniex ();
$bittrex  = new \ccxt\bittrex  (array ('verbose' => true));
$quoinex  = new \ccxt\quoinex   ();
$zaif     = new \ccxt\zaif     (array (
    'apiKey' => 'YOUR_PUBLIC_API_KEY',
    'secret' => 'YOUR_SECRET_PRIVATE_KEY',
));
$hitbtc   = new \ccxt\hitbtc   (array (
    'apiKey' => 'YOUR_PUBLIC_API_KEY',
    'secret' => 'YOUR_SECRET_PRIVATE_KEY',
));

$exchange_id = 'binance';
$exchange_class = "\\ccxt\\$exchange_id";
$exchange = new $exchange_class (array (
    'apiKey' => 'YOUR_API_KEY',
    'secret' => 'YOUR_SECRET',
));

$poloniex_markets = $poloniex->load_markets ();

var_dump ($poloniex_markets);
var_dump ($bittrex->load_markets ());
var_dump ($quoinex->load_markets ());

var_dump ($poloniex->fetch_order_book ($poloniex->symbols[0]));
var_dump ($bittrex->fetch_trades ('BTC/USD'));
var_dump ($quoinex->fetch_ticker ('ETH/EUR'));
var_dump ($zaif->fetch_ticker ('BTC/JPY'));

var_dump ($zaif->fetch_balance ());

// sell 1 BTC/JPY for market price, you pay ¥ and receive ฿ immediately
var_dump ($zaif->id, $zaif->create_market_sell_order ('BTC/JPY', 1));

// buy BTC/JPY, you receive ฿1 for ¥285000 when the order closes
var_dump ($zaif->id, $zaif->create_limit_buy_order ('BTC/JPY', 1, 285000));

// set a custom user-defined id to your order
$hitbtc->create_order ('BTC/USD', 'limit', 'buy', 1, 3000, array ('clientOrderId' => '123'));
.net/C#
using ccxt; // importing ccxt
namespace Project;
class Project {
    public async static Task CreateOrder() {
        var exchange = new Binance();
        exchange.apiKey = "my api key";
        exchange.secret = "my secret";
        // always use the capitalized method (CreateOrder instead of createOrder)
        var order = await exchange.CreateOrder("BTC/USDT", "limit", "buy", 1, 50);
        Console.WriteLine("Placed Order, order id: " + order.id);
    }
}
Contributing

Please read the CONTRIBUTING document before making changes that you would like adopted in the code. Also, read the Manual for more details.

Support Developer Team

We are investing a significant amount of time into the development of this library. If CCXT made your life easier and you want to help us improve it further, or if you want to speed up development of new features and exchanges, please support us with a tip. We appreciate all contributions!

Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website.

[Become a sponsor]

         

Supporters

Support this project by becoming a supporter. Your avatar will show up here with a link to your website.

[Become a supporter]

         

Backers

Thank you to all our backers! [Become a backer]

Thank you!

Social
 Follow us on Twitter
 Read our blog on Medium
 Join our Discord
 CCXT Channel on Telegram (important announcements)
 CCXT Chat on Telegram (technical support)
Star History

Contact Us

For business inquiries: info@ccxt.trade

About

A JavaScript / TypeScript / Python / C# / PHP cryptocurrency trading API with support for more than 100 bitcoin/altcoin exchanges

docs.ccxt.com
Topics
api bot library crypto bitcoin trading ethereum cryptocurrency exchange e-commerce market-data strategy btc cryptocurrencies trade eth arbitrage altcoin merchant invest
Resources
 Readme
License
 MIT license
 Activity
 Custom properties
Stars
 33.9k stars
Watchers
 938 watching
Forks
 7.6k forks
Report repository


Releases 122
4.4.45
Latest
+ 121 releases


Sponsor this project
opencollective.com/ccxt


Packages
No packages published



Used by 5.3k
+ 5,318


Contributors
695
+ 681 contributors


Languages
Python
27.8%
 
C#
24.9%
 
TypeScript
17.1%
 
JavaScript
16.4%
 
PHP
13.8%
 
C
0.0%
Footer
© 2025 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information