# flask 클론 코딩

## how to run

```powershell
# powershell
(pip install poetry) -and (poetry install)
poetry run flask run
```

```bash
# bash
# 환경변수까지 자동으로 지정
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
poetry install
poetry run flask run
```

## done

- flask 클론코딩
- poetry 연동
- .flaskenv 연동
- ec2 linux환경으로 실행가능하게 만들기

## todo

- db 연동(csv -> sqlite3)
- 리팩토링(flask 컨벤션으로 모듈화)
