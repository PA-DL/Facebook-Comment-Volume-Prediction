import requests


url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={
    "Page_likes": 6983,
    "Chekins":4000,
    "Returns":5,
    "Category":19,
    "C1":41,
    "C2":30,
    "C3":3,
    "C4":7,
    "C5":27,
    "BaseTime":34,
    "Length":178,
    "Shares":134,
    "hrs":24,
    "sun_pub": 0,
    "mon_pub": 1,
    "tue_pub": 0,
    "wed_pub": 0,
    "thu_pub": 0,
    "fri_pub": 0,
    "sat_pub": 0,
    "sun_base": 0,
    "mon_base": 0,
    "tue_base": 1,
    "wed_base": 0,
    "thu_base": 0,
    "fri_base": 0,
    "sat_base": 0
})

print(r.json())




