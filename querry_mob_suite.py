from mob_suite import cursor

def getAll():
    cursor.execute(
        """
        SELECT * FROM inctype
        """
    )
    for row in cursor.fetchall()[0:10]:
        print(row)

def getOne(id):
    cursor.execute(
        f"""
        SELECT * FROM inctype 
        WHERE sample_id = {id}
        """
    )
    result = cursor.fetchall()[0]
    print(result)

def subquery(col,query):
    cursor.execute(
        f"""
        SELECT * FROM inctype
        WHERE {col} = {query}
        """
    )

    results = cursor.fetchall()[0]

    for row in results:
        print(row)

if __name__ == "__main__":
    getAll()