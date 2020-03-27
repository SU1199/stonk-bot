# Stonk Bot
Bot which fetches latest stock info from yahoo finance and reports back on telegram.
## Usage

### Server Deployment
- Install the following python dependencies to your remote instance =>
--Python 3.x
--[TelegramPython wrapper]([https://github.com/python-telegram-bot/python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)) 
--Requests 
--BeautifulSoup 
- Clone this repository and run tradebot.py using python3. Disown the process from the terminal to keep it running in the background.
> python3 tradebot.py & disown
 ### Local VirtualEnv Deployment
 - Clone this repositiory and cd into it.
 - Use pipenv to open the virualenv.
 > pipenv shell
- Run the tradebot script and disown from terminal.
> python3 tradebot.py & disown
## Working

- The dataFetch.py script scrapes the data from yahoo finance website using requests and bs4 (beautifulSoup4)
- Uses TelegramPython library (basically an easy to use wrapper for python api) to communicate with the end user. 

## Further Improvements

Convert dataFetch.py to a fully-fledged and robust library with features like
 - Charting
 - Historical 10/20 year data.
 - Live updates from google finance api.
 - Futures and options info.
 - JSON responses.

