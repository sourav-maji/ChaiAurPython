import requests

def freeApi_get_random_dog():
    url = "https://api.freeapi.app/api/v1/public/dogs/dog/random"
    response = requests.get(url=url)
    data = response.json()
    if data["success"] and "data" in data:
        breed_group = data["data"]["breed_group"]
        life_span = data["data"]["life_span"]
        return breed_group , life_span
    else:
        raise Exception("Failed to fectch Dog data")
def main():
    try:
       bread, life =  freeApi_get_random_dog()
       print(f"Bread and life spans are : {bread}  & {life}")
    except Exception as e:
        print(f"Exception is : {str(e)}")
    
if __name__ =="__main__":
    main()