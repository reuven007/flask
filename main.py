from webpage import app

if __name__ == '__main__':
    app.run(debug=True)



# @app.get("/item/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "query": q}
