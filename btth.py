from fastapi import FastAPI , HTTPException

app=FastAPI(
    title= "Mini API danh sách khóa học với FastAPI",
    description= " hệ thống quản lí khóa học",
    version= '1.0.0'
)

courses = [
    {
        "id": 1,
        "code": "PY101",
        "name": "Python Basic",
        "level": "beginner",
        "price": 1500000
    },
    {
        "id": 2,
        "code": "FA101",
        "name": "FastAPI Basic",
        "level": "beginner",
        "price": 2000000
    }
]

@app.get("/health")
def get_check():
    return {"message": "API is running"}

@app.get("/courses")
def get_list():
    return courses

@app.get("/courses/{course_id}")
def get_courses_id(course_id : int):
    if course_id < 0:
        raise HTTPException(
            status_code = 400,
            detail= "course_id không dc < hơn 0"
        )
    for i in courses:
        if course_id == i["id"]:
            return i
    else:
        raise HTTPException(
            status_code= 404,
            detail= "Không tìm thấy khóa học"
        )