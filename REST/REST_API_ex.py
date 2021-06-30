import requests


if __name__ == '__main__':
    # REST API 경로에 접속하여 응답(Response) 데이터 받아오기
    target = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url=target)

    # 응답(Response) 데이터가 JSON 형식이므로 바로 파이썬 객체로 변환
    data = response.json()

    # 모든 사용자(user) 정보를 확인하며 이름 정보만 삽입
    name_list = []
    address_list = []
    for user in data:
        name_list.append(user['name'])
        address_list.append(user['address'])
    print(name_list)
    print(address_list)
