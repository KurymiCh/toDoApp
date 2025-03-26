from app.db.engine import session

def get_db():
    try:
        yield db 
    finally:
        db.close()