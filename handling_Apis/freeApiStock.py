import requests

def get_free_api_stock_market():
    url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"
    response  = requests.get(url=url)
    data = response.json()
    if data["success"] and "data" in data:
        TATACHEM = data["data"]["data"][0]["CurrentPrice"]
        # print(f"TATACHEM price is :  {TATACHEM}")
        TATACOFFEE  =data["data"]["data"][1]["CurrentPrice"]
        # print(f"TATACOFFEE price is : {TATACOFFEE}")
        return TATACHEM ,TATACOFFEE
    else:
        raise Exception("Failed to fetch Stock Data")


def main():
    try:
        tatachem , tatacoffee = get_free_api_stock_market()
        print(f"TATACHEM  & TATACOFFEE price are :  {tatachem} & {tatacoffee}")
    except Exception as e:
        print(f"Exception is {str(e)}")

if __name__ == "__main__":
    main()

