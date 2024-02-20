import requests

def fetch_random_user_from_freeApi():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url=url)
    data = response.json()
    # print(f"Response is ::: {data} ", type(data))
    if data["success"] and "data" in data:
        user_data = data['data']
        user_name = user_data["login"]["username"]
        country = user_data["location"]["country"]
        print(f"User name is : {user_name} & Country is :  {country}" )
        return user_name, country
    else:
        raise Exception("Fail to fetch user data")

def main():
    try:
        user_name , country = fetch_random_user_from_freeApi()
        print(f"User Name : {user_name} \nCountry : {country}")
    except Exception as e:
        print("Exception is : {str(e)}")
if __name__ == "__main__":
    main()