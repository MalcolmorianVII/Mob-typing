from mob_suite import cursor

def getAll():
    cursor.execute(
        """
        SELECT * FROM inctype
        """
    )

def getOne(id):
    cursor.execute(
        f"""
        SELECT * FROM inctype 
        WHERE sample_id = {id}
        """
    )

def subquery(col,query):
    cursor.execute(
        f"""
        SELECT * FROM inctype
        WHERE {col} = {query}
        """
    )

if __name__ == "__main__":
    getAll()