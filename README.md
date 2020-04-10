# moviedb

GraphQL facade for fetching movies from IMDB through http://www.omdbapi.com/

to run this API run
`docker-compose build; docker-compose up`

go to
`http://localhost:8000/graphql/`

to fetch movie by IMDB id or title, use:
```.graphql
{
  movieFetch(imdbid: "IMDB id", title: "movie title", mtype: MovieTypeEnum, year: "year", plot: PlotTypeEnum) {
    movie {
        title
        year
        rated
        released
        runtime
        genre
        director
        writer
        actors
        plot
        language
        country
        awards
        poster
        ratings
        metascore
        imdbrating
        imdbvotes
        imdbid
        type
        dvd
        boxoffice
        production
        website
    }
    errors {
      message
      field
    }
  }
}
```

where 
`MovieTypeEnum`:
```
  MOVIE
  SERIES
  EPISODE
```
`PlotTypeEnum`:
```
  SHORT
  FULL
```

to search for movie, use
```.graphql
{
  movieSearch(title: "title", mtype: MovieTypeEnum, year: "year", page: <page number>) {
    movies {
        title
        year
        rated
        released
        runtime
        genre
        director
        writer
        actors
        plot
        language
        country
        awards
        poster
        ratings
        metascore
        imdbrating
        imdbvotes
        imdbid
        type
        dvd
        boxoffice
        production
        website
    }
    errors {
      message
      field
    }
  }
}

```


to save movie to local DB, use
