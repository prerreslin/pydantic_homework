from main import app
from db import Session,Movie
from fastapi import HTTPException
from schemas import MovieModel

@app.get("/get_movies")
def get_movies():
    with Session() as session:
        movies = session.query(Movie).all()
        return movies
    

@app.post("/add_movie")
def add_movie(data:MovieModel):
    with Session() as session:
        movie = session.query(Movie).where(Movie.title==data.title).first()
        if movie:
            raise HTTPException(status_code=409,detail="Conflict")
        
        new_movie = Movie(
            title=data.title,
            director=data.director,
            release_year=data.release_year
        )

        session.add(new_movie)
        session.commit()
        session.refresh(new_movie)
        return new_movie


@app.get("/get_movie/{id}")
def get_movie(id):
    with Session() as session:
        movie = session.query(Movie).where(Movie.id==id).first()
        if not movie:
            raise HTTPException(status_code=404,detail="Movie not found")
        return movie
    

@app.delete("/delete_movie/{id}")
def delete_movie(id):
    with Session() as session:
        movie = session.query(Movie).where(Movie.id==id).first()
        if not movie:
            raise HTTPException(status_code=404,detail="Movie not found")
        
        session.delete(movie)
        session.commit()
        return {"Message":"Movie deleted"}