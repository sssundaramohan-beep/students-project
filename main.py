# from fastapi import FastAPI
# from pydantic import BaseModel
# import psycopg2

# app = FastAPI()

# def get_connection():
#     return psycopg2.connect(
#         host="localhost",
#         database="chit_fund",
#         user="postgres",
#         password="12345"
#     )

# class Member(BaseModel):
#     member_id: int
#     name: str



# @app.get("/members")
# def get_members():
#     conn = get_connection()
#     cur = conn.cursor()

#     cur.execute("SELECT member_id, name FROM members")
#     rows = cur.fetchall()

#     members = [{"member_id": r[0], "name": r[1]} for r in rows]

#     cur.close()
#     conn.close()

#     return members




# @app.post("/members")
# def add_member(member: Member):
#     conn = get_connection()
#     cur = conn.cursor()

#     query = """INSERT INTO members (member_id, name) VALUES (%s, %s)"""
#     cur.execute(query, (member.member_id, member.name))
#     conn.commit()

#     cur.close()
#     conn.close()

#     return {"message": "Member added successfully"}



# @app.put("/members/{member_id}")
# def update_member(member_id: int, member: Member):
#     conn = get_connection()
#     cur = conn.cursor()

#     query = """UPDATE members SET name = %s WHERE member_id = %s"""
#     cur.execute(query, (member.name, member_id))
#     conn.commit()

#     cur.close()
#     conn.close()

#     return {"message": "Member updated successfully"}



# @app.delete("/members/{member_id}")
# def delete_member(member_id: int):
#     conn = get_connection()
#     cur = conn.cursor()

#     cur.execute("DELETE FROM members WHERE member_id = %s", (member_id,))
#     conn.commit()

#     cur.close()
#     conn.close()

#     return {"message": "Member deleted successfully"}



