from app import db

belt_to_song_dict = {
    "None": ["Hot Cross Buns", "White"],
    "White": ["Gently Sleep", "Yellow"],
    "Yellow": ["Merrily We Roll Along", "Orange"],
    "Orange": ["It's Raining", "Green"],
    "Green": ["Old MacDonald Had a Farm", "Purple"],
    "Purple": ["When The Saints Go Marching In", "Blue"],
    "Blue": ["Twinkle, Twinkle Little Star", "Red"],
    "Red": ["Amazing Grace", "Brown"],
    "Brown": ["Ode To Joy", "Black"],
    "Black": ["None", None]
}

def fetch_records(search_val: str) -> dict:
    to_search = False
    arr_searches = search_val.split("_")
    for i in arr_searches:
        if len(i) != 0:
            to_search = True
            break

    if to_search == 0:
        conn = db.connect()
        load_results = conn.execute("Select * from Student JOIN Progress ON Student.Progress_ID = Progress.Progress_ID ORDER BY Student.Student_ID DESC;").fetchall()
        conn.close()
        records_list = []
        for p in load_results:
            name = p[1] + " " + p[2]
            item = {
            "id": p[0],
            "name": name,
            "period": p[3],
            "task": p[7],
            "song": p[8],
            }
            records_list.append(item)
        return records_list
    else:
        conn = db.connect()
        search_results = None
        if (arr_searches[0] != '' and arr_searches[1] != '' and arr_searches[2] != '' and arr_searches[3] != ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where next_song like '%%"+arr_searches[3]+"%%' AND current_belt like '%%"+arr_searches[2]+"%%' AND class_period like '%%"+arr_searches[1]+"%%' AND first_name like '%%"+arr_searches[0]+"%%';").fetchall()
        elif (arr_searches[0] != '' and arr_searches[1] != '' and arr_searches[2] != '' and arr_searches[3] == ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where current_belt like '%%"+arr_searches[2]+"%%' AND class_period like '%%"+arr_searches[1]+"%%' AND first_name like '%%"+arr_searches[0]+"%%';").fetchall()
        elif (arr_searches[0] != '' and arr_searches[1] != '' and arr_searches[2] == '' and arr_searches[3] == ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where class_period like '%%"+arr_searches[1]+"%%' AND first_name like '%%"+arr_searches[0]+"%%';").fetchall()
        elif (arr_searches[0] != '' and arr_searches[1] == '' and arr_searches[2] == '' and arr_searches[3] == ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where first_name like '%%"+arr_searches[0]+"%%';").fetchall()
        elif (arr_searches[0] == '' and arr_searches[1] != '' and arr_searches[2] != '' and arr_searches[3] != ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where next_song like '%%"+arr_searches[3]+"%%' AND current_belt like '%%"+arr_searches[2]+"%%' AND class_period like '%%"+arr_searches[1]+"%%';").fetchall()
        elif (arr_searches[0] == '' and arr_searches[1] == '' and arr_searches[2] != '' and arr_searches[3] != ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where next_song like '%%"+arr_searches[3]+"%%' AND current_belt like '%%"+arr_searches[2]+"%%';").fetchall()
        elif (arr_searches[0] == '' and arr_searches[1] == '' and arr_searches[2] == '' and arr_searches[3] != ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where next_song like '%%"+arr_searches[3]+"%%';").fetchall()
        elif (arr_searches[0] == '' and arr_searches[1] == '' and arr_searches[2] != '' and arr_searches[3] == ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where current_belt like '%%"+arr_searches[2]+"%%';").fetchall()
        elif (arr_searches[0] == '' and arr_searches[1] != '' and arr_searches[2] != '' and arr_searches[3] == ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where current_belt like '%%"+arr_searches[2]+"%%' AND class_period like '%%"+arr_searches[1]+"%%';").fetchall()
        elif (arr_searches[0] != '' and arr_searches[1] == '' and arr_searches[2] != '' and arr_searches[3] == ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where current_belt like '%%"+arr_searches[2]+"%%' AND first_name like '%%"+arr_searches[0]+"%%';").fetchall()
        elif (arr_searches[0] != '' and arr_searches[1] == '' and arr_searches[2] == '' and arr_searches[3] != ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where first_name like '%%"+arr_searches[0]+"%%' AND next_song like '%%"+arr_searches[3]+"%%';").fetchall()
        elif (arr_searches[0] == '' and arr_searches[1] != '' and arr_searches[2] == '' and arr_searches[3] != ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where class_period like '%%"+arr_searches[1]+"%%' AND next_song like '%%"+arr_searches[3]+"%%';").fetchall()
        elif (arr_searches[0] != '' and arr_searches[1] != '' and arr_searches[2] == '' and arr_searches[3] != ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where first_name like '%%"+arr_searches[0]+"%%' AND class_period like '%%"+arr_searches[1]+"%%' AND next_song like '%%"+arr_searches[3]+"%%';").fetchall()
        elif (arr_searches[0] != '' and arr_searches[1] == '' and arr_searches[2] != '' and arr_searches[3] != ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where first_name like '%%"+arr_searches[0]+"%%' AND next_song like '%%"+arr_searches[3]+"%%';").fetchall()
        elif (arr_searches[0] == '' and arr_searches[1] != '' and arr_searches[2] == '' and arr_searches[3] == ''):
            search_results = conn.execute("select * from Progress NATURAL JOIN Student where class_period like '%%"+arr_searches[1]+"%%';").fetchall()

        conn.close()
        search_list = []
        for s in search_results:
            name = s[4] + " " + s[5]
            item = {
                "id": s[0],
                "name": name,
                "period": s[6],
                "task": s[1],
                "song": s[2]
            }
            search_list.append(item)

        return search_list


def update_belt_entry(record_id: int, data: dict) -> None:
    conn = db.connect()
    first_name = data['first_name']
    last_name = data['last_name']
    period = data['period']
    belt = data['belt']
    if belt:
        song = belt_to_song_dict[belt][0]
    if len(first_name):
        query = 'UPDATE Student SET first_name = "{}" WHERE student_ID = {};'.format(first_name, record_id)
        conn.execute(query)
    if len(last_name):
        query = 'UPDATE Student SET last_name = "{}" WHERE student_ID = {};'.format(last_name, record_id)
        conn.execute(query)
    if len(period):
        query = 'UPDATE Student SET class_period = "{}" WHERE student_ID = {};'.format(period, record_id)
        conn.execute(query)
    if len(belt):
        query = 'UPDATE Progress SET current_belt = "{}", next_song = "{}" WHERE progress_ID = {};'.format(belt, song, record_id)
        conn.execute(query)

    conn.close()

def update_status_entry(record_id: int) -> None:
    conn = db.connect()
    get_query = 'SELECT * FROM Progress WHERE progress_ID = {};'.format(int(record_id))
    progress_query_results = conn.execute(get_query)
    progress_query_results = [x for x in progress_query_results]
    # Get current_belt
    current_belt = progress_query_results[0][1]
    if current_belt == "Black":
        return
    next_belt = belt_to_song_dict[current_belt][1]
    next_song = belt_to_song_dict[next_belt][0]
    update_query = 'UPDATE Progress SET current_belt = "{}", next_song = "{}" WHERE progress_ID = {};'.format(next_belt, next_song, record_id)
    conn.execute(update_query)
    conn.close()

def insert_new_record(first_name: str, last_name: str, class_period: str, belt: str, student_teacher_id: str) -> int:
    next_song = belt_to_song_dict[belt][0]
    conn = db.connect()


    progress_query = 'Insert Into Progress (current_belt, next_song) VALUES ("{}", "{}")'.format(belt, next_song)
    conn.execute(progress_query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    print("TASK ID: ", task_id)
    student_query = 'Insert Into Student (student_ID, first_name, last_name, class_period, progress_ID, teacher_ID) VALUES ("{}", "{}", "{}", "{}", "{}", "{}");'.format(int(task_id), first_name, last_name, class_period, int(task_id), int(student_teacher_id))
    conn.execute(student_query)
    conn.close()
    # conn.execute(query)
    # conn.close()
    # return task_id

def remove_record_by_id(task_id: int) -> None:
    conn = db.connect()
    delete_student_query = 'DELETE FROM Student WHERE (student_ID = "{}");'.format(task_id)
    conn.execute(delete_student_query)
    delete_progress_query = 'DELETE FROM Progress WHERE (progress_ID = "{}");'.format(task_id)
    conn.execute(delete_progress_query)
    conn.close()

def run_advanced_query() -> dict:
    conn = db.connect()
    advanced_query = '''
    SELECT t.first_name, t.last_name, COUNT(p.current_belt) AS num_black_belts
    FROM records.Teacher t JOIN records.Student s ON s.teacher_ID = t.teacher_ID JOIN records.Progress p ON s.progress_ID = p.progress_ID
    WHERE p.current_belt like "Black"
    GROUP BY t.first_name, t.last_name
    ORDER BY t.last_name
    LIMIT 0, 15;
    '''
    search_results = conn.execute(advanced_query).fetchall()
    conn.close()
    teacher_list = []
    for p in search_results:
        name = p[0] + " " + p[1]
        teacher = {
         "name": name,
         "num_black_belts": p[2],
        }
        teacher_list.append(teacher)
    return teacher_list