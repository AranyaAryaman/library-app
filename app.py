from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Database connection config
DB_HOST = "localhost"
DB_NAME = "library"
DB_USER = "aranya"
DB_PASS = ""  # If you have a password, set it here.

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        mid = request.form['mid']
        return redirect(url_for('loans', mid=mid))
    return render_template('home.html')

@app.route('/loans/<mid>')
def loans(mid):
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        SELECT 
            b.bid,
            b.title,
            b.genre,
            b.year,
            lb.lid,
            lb.lname,
            lb.laddress,
            bc.copyid,
            l.loandate,
            l.returndate
        FROM 
            Loan l
        JOIN 
            book_copy bc ON l.copyid = bc.copyid
        JOIN 
            Book b ON bc.bid = b.bid
        JOIN 
            library_branch lb ON bc.lid = lb.lid
        WHERE 
            l.mid = %s;
    """
    cur.execute(query, (mid,))
    loans = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('loans.html', loans=loans, mid=mid)

@app.route('/available/<bid>')
def available(bid):
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        SELECT 
            bc.copyid,
            lb.lid,
            lb.lname,
            lb.laddress
        FROM 
            book_copy bc
        JOIN 
            library_branch lb ON bc.lid = lb.lid
        LEFT JOIN 
            Loan l ON bc.copyid = l.copyid AND l.returndate IS NULL
        WHERE 
            bc.bid = %s
            AND l.copyid IS NULL;
    """
    cur.execute(query, (bid,))
    copies = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('available.html', copies=copies, bid=bid)

if __name__ == '__main__':
    app.run(debug=True)
