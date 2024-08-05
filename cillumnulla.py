from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate

app = FastAPI()

# Assuming you have a Todo model and a todos table in your database

@app.get('/todos')
def get_todos(db: Session = Depends(get_db), page: int = 1):
    items_per_page = 10  # Set the number of items to display per page
    todos = db.query(Todo).all()  # Retrieve all todos from the database
    paginated_todos = paginate(todos, page, items_per_page)  # Paginate the todos
    return paginated_todos

# Other routes and dependencies...

