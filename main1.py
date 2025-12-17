from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="chit_fund",
        user="postgres",
        password="1234567"
    )



@app.post("/add-chit-member")
def add_chit_member(chit_member_id: int,chit_id: int,member_id: int,joined_date: str):
    conn = get_connection()
    cur = conn.cursor()

    sql = '''
            insert into chit_members(chit_member_id,chit_id,member_id,joined_date) 
            values (%s,%s,%s,%s) returning chit_member_id
    '''
            
    cur.execute(sql, (chit_member_id,chit_id,member_id,joined_date))

    conn.commit()
    affected = cur.rowcount

    cur.close()
    conn.close()

    if affected == 0:
        return {"message": "No record found", "Insert": 0}

    return {"message": "Record Added successfully", "Insert": affected}


@app.put("/update-chit-member/{chit_member_id}")
def update_chit_member(
    chit_member_id: int,
    chit_id: int,
    member_id: int,
    joined_date: str
):
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        UPDATE chit_member
        SET chit_id = %s,
            member_id = %s,
            joined_date = %s
        WHERE chit_member_id = %s
    """

    cur.execute(sql, (chit_id, member_id, joined_date, chit_member_id))
    conn.commit()

    affected = cur.rowcount
    cur.close()
    conn.close()

    if affected == 0:
        return {"message": "No record found", "updated": 0}
    return {"message": "Updated successfully", "updated": affected}




@app.delete("/delete-chit-member/{chit_member_id}")
def delete_chit_member(chit_member_id: int):
    conn = get_connection()
    cur = conn.cursor()

    sql = "DELETE FROM chit_member WHERE chit_member_id = %s"
    cur.execute(sql, (chit_member_id,))

    conn.commit()
    affected = cur.rowcount

    cur.close()
    conn.close()

    if affected == 0:
        return {"message": "No record found", "deleted": 0}

    return {"message": "Deleted successfully", "deleted": affected}