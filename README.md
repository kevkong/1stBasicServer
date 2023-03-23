# 1stBasicServer
## 1.1 Instruction for running the app.
python .\App.py
The web service will run at port 5000 e.g. http://127.0.0.1:5000

## 1.2 Instruction for testing the app.
Ran on VS Code:
### Add item to database:
'curl -X POST -H "Content-Type: application/json" -d '{\"title\":\"Buy groceries\", \"completed\":0}' http://localhost:5000/todos'

### Get all item in database:
'curl http://localhost:5000/todos'

### Change item status
'curl -X PUT http://localhost:5000/todos/1/completed'

### Delete item
'curl -X DELETE http://localhost:5000/todos/1'

1.3 Instruction for building the app
N/A

1.4 interface documentation
---
List API
```http
GET /todos
```
Responses:
```json
[
    {
        "id": integer,
        "title": string,
        "completed": bool
    },
]
```
---
Create API
```http
POST /todos
```
Request:
```json
{
    "title": string,
    "completed": string
}
```
Responses:
"", 201
---
Update API
```http
PUT /todos/update/{id}/<column>
```
No request body required
---
Delete API
```http
DELETE /todo/delete/{id}
```
No request body required
