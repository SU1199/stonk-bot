import logging
import telegram
from telegram.error import NetworkError, Unauthorized
import dataFetch

update_id = None
instructions = "Enter '$<ticker> x' where x can be \nsum => summary \nltp => Last Traded Price \nmktcap => Market Cap \nchg => Day's price change \nprevclose => Previous Close Price \nopenprice => Opening Price \ndayrange => Day's price range \n52range => 52 Week Range\nvol => volume\npe => P/E Ratio \ndiv => Dividend Yields \n Example => $SPY sum \n Example-2 => $HDFCBANK.NS ltp"
def main():
    global update_id
    bot = telegram.Bot('TOKEN')
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            responder(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1


def responder(bot):
    global update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:
            if update.message.text.lower().split(" ",1)[0][0] == "$":
                if len(update.message.text.lower().split(" ",1)) == 2:
                    ticker = update.message.text.lower().split(" ",1)[0][1:]
                    command = update.message.text.lower().split(" ",1)[1]
                    update.message.reply_text(alpha(ticker,command))
                else:
                    update.message.reply_text(instructions)
            else:
                update.message.reply_text(instructions)

def alpha(ticker,command):
    if command == "sum":
        return dataFetch.summary(ticker)
    elif command == "ltp":
        return dataFetch.lastTradedPrice(ticker)
    elif command == "mktcap":
        return dataFetch.marketCap(ticker)
    elif command == "chg":
        return dataFetch.change(ticker)
    elif command == "prevclose":
        return dataFetch.previousClose(ticker)
    elif command == "openprice":
        return dataFetch.openPrice(ticker)
    elif command == "dayrange":
        return dataFetch.daysRange(ticker)
    elif command == "52range":
        return dataFetch.fiftyTwoRange(ticker)
    elif command == "vol":
        return dataFetch.volume(ticker)
    elif command == "pe":
        return dataFetch.peRatio(ticker)
    elif command == "div":
        return dataFetch.dividend(ticker)
    else:
        return "Invalid Command"

if __name__ == '__main__':
    main()
