from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests, logging, math


logging.basicConfig(level = logging.INFO)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods =["GET"],
    allow_headers=["*"]
)


url = "http://numbersapi.com/{}/math"
def is_armstrong(n:int):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n


def even(n:int):
    """Check if a number is even."""
    return n % 2 == 0

def properties (n:int):
    props = []
    if is_armstrong(n):
        props.append("armstrong")
    if even(n):
        props.append("even")
    else:
        props.append("odd")
    return props

    # if even and is_armstrong:
    #     properties =["armstrong","even"]
    #     return properties
    # elif not(even) and is_armstrong:
    #     properties = ["armstrong", "odd"]
    #     return properties
    # elif even and not is_armstrong:
    #     properties=['even']
    #     return properties
    # elif not even and not is_armstrong:
    #     properties = ['odd']
    #     return properties


def digit_sum(n:int):
    """Calculate the sum of the digits of a number."""
    return sum(int(digit) for digit in str(n))
def perfect_square(n:int):
    """Check if a number is a perfect square."""
    if n < 0:
        return False
    sqrt = math.sqrt(n)
    return sqrt == int(sqrt)


def is_prime(n: int):
    """ check for """
    if n < 2:
        return False
    if n in (2,3):
        return True
    if n % 2 == 0 or n % 3==0:
        return False
    i = 5
    while i *i <= n:
        if n % i ==0 or n %(i + 2)==0:
            return False
        i +=6 
    return True
    
    
@app.get ("/api/classify-number")
def num_check(number: str):

    try:
        number_int = int(number)
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    # Fetch fun fact about the number from Numbers API
    try:
        response = requests.get(url.format(number_int))
        if response.status_code == 200:
            return {
                "number": number_int,
                "is_prime": is_prime(number_int),
                "is_perfect": perfect_square(number_int),
                "properties": properties(number_int),
                "digit_sum": digit_sum(number_int),
                "fun_fact": response.text
            }
        else:
            raise HTTPException(status_code=400, detail="Failed to fetch fun fact.")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Error connecting to Numbers API.")
    # try :
    #     response =requests.get(url.format(number))
    #     logging.info(f"API response: {response.status_code}-{response.text}")
    #     if response.status_code >= 400:
    #         return {
    #             "number":"alphabet",
    #             "error": "failed to fetch data from number api", "status code": response.status_code}

    #     return  {
    #             "number":number, 
    #             "is_prine":is_prime(number),
    #             "is_perfect": perfect_square(number),
    #             "properties":properties(number),
    #             "digit_sum": digit_sum(number),
    #             "fact":response.text
    #             }
    # except Exception as e:
    #     logging.error(f"Error fetching  number fact : {e} ")
    #     return {
    #             "number":"alphabet",
    #             "error": "failed to fetch data from number api", "status code": response.status_code}

