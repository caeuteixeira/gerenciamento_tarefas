import sqlite3

DB_PATH = './todo.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

#create
def add_to_list(item):
    try:
        connect = sqlite3.connect(DB_PATH)
        cursor = connect.cursor()
        cursor.execute('insert into items(item, status) values (?, ?)', (item, NOTSTARTED))
        connect.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None

#read
def get_all_items():
    try:
        connect = sqlite3.connect(DB_PATH)
        cursor = connect.cursor()
        cursor.execute('select * from items')
        rows = cursor.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None
    
def get_item(item):
    try:
        connect = sqlite3.connect(DB_PATH)
        cursor = connect.cursor()
        cursor.execute("select status from items where item='%s'" % item)
        status = cursor.fetchone()[0]
        return status
    except Exception as e:
        print('Error: ', e)
        return None
    
#update
def update_status(item, status):
    if(status.lower().strip() == 'not started'):
        status = NOTSTARTED
    elif (status.lower().strip() == 'in progress'):
        status = INPROGRESS
    elif (status.lower().strip() == 'completed'):
        status = COMPLETED
    else:
        print("Invalid Status: " + status)
        return None
    
    try:
        connect = sqlite3.connect(DB_PATH)
        cursor = connect.cursor()
        cursor.execute('update items set status=? where item=?', (status, item))
        connect.commit()
        return {item: status}
    except Exception as e:
        print('Error: ', e)
        return None
    
#delete
def delete_item(item):
    try:
        connect = sqlite3.connect(DB_PATH)
        cursor = connect.cursor()
        cursor.execute('delete from items where item=?', (item,))
        connect.commit()
        return {'item': item}
    except Exception as e:
        print('Error: ', e)
        return None