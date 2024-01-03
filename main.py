from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

app = FastAPI()
templates = Jinja2Templates(directory ="templates")

@app.get("/")
def index(request:Request):
    return templates.TemplateResponse(
        "login.html", {
            "request" : request
        }
    )


class UserInfoModel(BaseModel):
    userid:str = Field()
    password:str = Field()


members = [
    {'userid' : 'sumin', 'password' : '1q2w3e4r'},
    {'userid' : 'daejoon', 'password' : '1234'}
]

@app.post('/login')
def login(request:Request, user_info:UserInfoModel):
    userid = user_info.userid
    password = user_info.password

    member = [m for m in members if m['userid'] == userid]
    if len(member) == 0:
        return {'msg': '회원정보가 없습니다.'}
    
    elif member[0]['password'] != password:
        return {'msg' : '패스워드가 일치하지 않습니다.'}
    
    else:
        return {'msg' : f'{userid} 고객님 환영합니다.'}

