import requests

def get_free_api_youtuble_channel():
    url = "https://api.freeapi.app/api/v1/public/youtube/channel"
    response  = requests.get(url=url)
    data = response.json()
    if data["success"] and "data" in data:
        title = data["data"]["info"]["brandingSettings"]["channel"]["title"]
        description = data["data"]["info"]["brandingSettings"]["channel"]["description"]
        # print(title , description)
        return title , description
    else:
        raise Exception("Fail to get Youtube channel data")


def main():
    try:
        channel_title , channel_description = get_free_api_youtuble_channel()
        print(f"channel_title & channel_description are {channel_title} \t {channel_description}")
    except Exception as e:
        print("Exception is str(e)")

if __name__ == "__main__":
    main()
