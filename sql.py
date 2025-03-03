

from dotenv import load_dotenv

load_dotenv()  ## Load all environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

## Configure Google Gemini API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt[0], question])
    return response.text


## Function To Retrieve Query from the Database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except sqlite3.Error as e:
        return [("Error:", str(e))]


## Ensure Table Exists Before Querying
def ensure_table_exists():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS STUDENT(
        NAME VARCHAR(25),
        CLASS VARCHAR(25),
        SECTION VARCHAR(25),
        MARKS INT);
    """)
    conn.commit()
    conn.close()


## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION, MARKS.\n\nFor example:
    - How many entries of records are present?
      SQL: SELECT COUNT(*) FROM STUDENT;
    - Tell me all the students studying in Data Science class?
      SQL: SELECT * FROM STUDENT WHERE CLASS="Data Science";

    **Do NOT include "```sql" or "```" in the response.**
    """
]

## 🎨 Streamlit App UI & UX Enhancements
st.set_page_config(page_title="Advanced SQL Query Generator", layout="wide")

# 🎯 Sidebar for Instructions & About
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2721/2721292.png", width=100)
    st.title("📌 How It Works")
    st.markdown(
        "1️⃣ **Enter a question in plain English**  \n"
        "2️⃣ **The AI converts it into an SQL query**  \n"
        "3️⃣ **The app fetches results from the database**  \n"
        "4️⃣ **You get an answer instantly! 🎯**"
    )

    st.warning("⚠️ **First, run all three files (sqlite.py, sqlite_copy.py, and sql.py) to ensure the database exists.** Then, ask your query.")
    st.markdown("---")
    st.write("👩‍💻 **Created By:** Prarthana 💙")

# 🎬 Animated Header
st.markdown(
    "<h1 style='text-align: center; color: #1f77b4;'>🎯 AI-Powered SQL Query Generator 🚀</h1>",
    unsafe_allow_html=True
)

# 📝 User Input
question = st.text_input("🔍 **Enter Your Question:**", key="input")

# 🎯 Button to Generate SQL Query
if st.button("🔎 Get SQL Query & Fetch Data"):
    if question:
        ensure_table_exists()  # Ensure table exists before querying

        with st.spinner("🤖 Generating SQL query..."):
            sql_query = get_gemini_response(question, prompt)

        st.success(f"✅ Generated Query: `{sql_query}`")

        # Fetch Data
        with st.spinner("📡 Fetching Data from Database..."):
            response = read_sql_query(sql_query, "student.db")

        if response:
            st.subheader("📊 **Query Results:**")
            for row in response:
                st.write(row)
        else:
            st.warning("⚠️ No data found in the database.")
    else:
        st.error("❌ Please enter a valid question.")

# ✨ Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>✨ Powered by Google Gemini Pro ✨</h4>", unsafe_allow_html=True)





