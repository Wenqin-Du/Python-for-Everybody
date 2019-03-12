SELECT Album.title, Artist.name 
FROM Album JOIN Artist 
ON Album.artist_id = Artist.id;

SELECT Track.title, Genre.name 
FROM Track JOIN Genre 
ON Track.genre_id = Genre.id;

SELECT Track.title, Artist.name, Album.title, Genre.name
FROM Track JOIN Album JOIN Genre JOIN Artist
ON Track.genre_id = Genre.id AND Track.album_id = Album.id AND Album.artist_id = Artist.id