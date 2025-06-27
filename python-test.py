# import requests

# url = "http://localhost:8000/heroes/"
# data = {
#     "name": "Superman",
#     "power": "Flight",
#     "city": "Metropolis",
#     "age": 30,
#     "is_active": True,
# }

# response = requests.post(url, json=data)
# print(response.json())

# print("Status Code:", response.status_code)
# print("Raw Text:", response.text)  # Show raw error text from backend

# # Only try to parse JSON if status is 200
# if response.headers.get("Content-Type") == "application/json":
#     try:
#         print("JSON:", response.json())
#     except Exception as e:
#         print("Failed to parse JSON:", e)
# else:
#     print("Server did not return JSON.")

# import requests

# url = "http://localhost:8000/heroes/"

# data = {
#     "name": "Superman",
#     "power": "Flight",
#     "city": "Metropolis",
#     "age": 30,
#     "is_active": True,
# }

# response = requests.post(url, json=data)

# print("Status Code:", response.status_code)
# print("Raw Text:", response.text)  # Show raw error text from backend

# # Only try to parse JSON if status is 200 and content type is JSON
# if response.headers.get("Content-Type", "").startswith("application/json"):
#     try:
#         print("JSON:", response.json())
#     except Exception as e:
#         print("Failed to parse JSON:", e)
# else:
#     print("Server did not return JSON.")

# from pydantic import BaseModel


# class Hero(BaseModel):
#     name: str
#     power: str
#     city: str
#     age: int
#     is_active: bool
