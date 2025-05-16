
def User(BaseModel):
    id = field(Integer,primarkey=True,autoincreamen=True)
    first_name= field(String)
app.post('/raw')
async def raw(request: Request,db=SessionManager):
    get_user = db.query(User.id).filter(User.id=request.id).all()
    if get_user:
        return True
    else:
        return False