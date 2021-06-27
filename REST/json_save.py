import json

# 사전 자료형(dict) 데이터 선언
user = [{
    "id": "gildong",
    "password": "1!2@3#4$",
    "age": 30,
    "hobby": ["football", "programming"]

    },
    {
    "id": "yeongkwon",
    "password": "1234",
    "age": 26,
    "hobby": ["baseball", "programming"]

    }]

if __name__ == '__main__':
    # JSON 데이터로 변환하여 파일로 저장
    with open("user.json", "w", encoding="utf-8") as file:
        json_data = json.dump(user, file, indent=4)
    print("### save sucessfully ###")