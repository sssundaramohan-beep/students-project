
from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="chit_fund",
        user="postgres",
        password="12345"
    )

@app.get("/company/{company_id}/members")
def get_members(company_id: int):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT 
            m.member_id,
            m.name,
            cm.chit_id,
            cm.joined_date
        FROM company_details c
        JOIN chit_detail cd ON cd.company_id = c.company_id
        JOIN chit_members cm ON cm.chit_id = cd.chit_id
        JOIN members m ON m.member_id = cm.member_id
        WHERE c.company_id = %s;
    """

    cur.execute(query, (company_id,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return {"company_id": company_id, "members": rows}





@app.post("/company")
def add_company(company_name: str, commission_percent: int):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO company_details (company_name, commission_percent)
        VALUES (%s, %s)
        RETURNING company_id;
    """

    cur.execute(query, (company_name, commission_percent))
    new_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    return {"message": "Company added successfully", "company_id": new_id}



@app.put("/company/{company_id}")
def update_company(company_id: int, company_name: str, commission_percent: int):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        UPDATE company_details
        SET company_name = %s,
            commission_percent = %s
        WHERE company_id = %s;
    """

    cur.execute(query, (company_name, commission_percent, company_id))
    conn.commit()

    cur.close()
    conn.close()

    return {"message": "Company updated successfully", "company_id": company_id}



@app.delete("/company/{company_id}")
def delete_company(company_id: int):
    conn = get_connection()
    cur = conn.cursor()

    query = "DELETE FROM company_details WHERE company_id = %s;"

    cur.execute(query, (company_id,))
    conn.commit()

    cur.close()
    conn.close()

    return {"message": "Company deleted successfully", "company_id": company_id}

