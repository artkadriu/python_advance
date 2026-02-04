import sqlite3
from typing

@router.get(path="/", response_model=List[Author])  # new *
def get_authors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select id, name from authors")
    authors = cursor.fetchall()
    conn.close()
    return [{"id": author[0], "name": author[1]} for author in authors]


@router.post(path="/", response_model=Author)  # new *
def create_author(author: AuthorCreate, _: str = Depends(get_api_key)):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("Insert into authors (name) values (?)", (author.name,))
        conn.commit()
        author_id = cursor.lastrowid
        return Author(id=author_id, name=author.name)
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"The author '{author.name}' already exists."
        )
    finally:
        conn.close()


@router.put(path="/{author_id}", response_model=Author)  # new *
def update_author(author_id: int, author: AuthorCreate, _: str = Depends(get_api_key)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("update authors set name = ? where id = ?", (author.name, author_id))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Author not found")
    conn.commit()
    conn.close()
    return Author(id=author_id, name=author.name)


@router.delete(path="/{author_id}", response_model=dict)  # new *
def delete_author(author_id: int, _: str = Depends(get_api_key)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("delete from authors where id = ?", (author_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Author not found")
    conn.commit()
    conn.close()
    return {"detail": "Author Deleted"}
