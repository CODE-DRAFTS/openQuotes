from app import main


def count_quotes():
    main.cursor.execute(""" SELECT COUNT(quote_id) FROM tbl_quotes """)
    count = main.cursor.fetchone()
    return int(count['count'])

def get_quote( quote_id: int ):
    main.cursor.execute(""" SELECT quote, author FROM tbl_quotes  WHERE quote_id=%s""", ( str(quote_id), ) )
    return main.cursor.fetchone()


def get_author_quotes( author_id: str , limit):
    if limit == None:
        main.cursor.execute(""" SELECT quote, author FROM tbl_quotes  WHERE author_id=%s""", ( str(author_id), ) )
        return main.cursor.fetchall()
    else:
        main.cursor.execute(""" SELECT quote, author FROM tbl_quotes  WHERE author_id=%s LIMIT %s""", ( str(author_id), str(limit), ) )
        return main.cursor.fetchall()


def get_authors():
    main.cursor.execute(""" SELECT * FROM authors  """ )
    return main.cursor.fetchall()