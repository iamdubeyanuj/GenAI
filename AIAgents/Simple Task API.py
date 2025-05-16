# Simple Task API
# Build a minimal FastAPI/Flask app with:
# POST /tasks: create task with a title
# GET /tasks/{id}: retrieve task by ID
# Use an in-memory store and Pydantic validation.


from fastapi import FastAPI
from pydentic.

class Task(BaseModel):
    id= field(Integer,autoincreamen=True)
    task_name = field(String)
    task_description = field(String)

def task_request(BaseModel):
    task_name:String
    task_description: String
app = FastAPI(docs_url='genai/')


# For getting Based on ID
app.get('/get_by_task_id/{id}')
def get_by_task_id(request:RequestData,db=SessionManager()):
    try:
        get_data= db.query(Task.id,Task.name).filter(Task.id=request.id).all()
        if get_data:
            return get_data
        else:
            return {'status':'Failed','message':'No Record found'}
    except Exception as ex:
        print(f'Error Found {ex}')
    finally:
        db.close()

# For Creating Record

app.post('/create_task'):
def create_record(request:task_request,db=SessionManager())
    create_data = (Task.task_name=task_request.task_name,task.task_description=task_request.task_descripion)
    db.add(create_data)
    db.commit()
