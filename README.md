# Power BI Project: Spotify Dashboard

## Table of Contents
- [Problem Statement](#problem-statement)
- [Data Discovery](#data-discovery)
- [Data Understanding](#data-understanding)
- [Data Cleaning and ETL](#data-cleaning-and-etl)
- [Data Modeling](#data-modeling)


# Problem Statement

This project aims to analyze the streaming performance and trends of the top 300 artists on Spotify using **Power BI**. With a rich dataset that includes track details, artist info, release dates and streaming numbers, the goal is to build an interactive dashboard that helps users:

- **Compare streaming stats** like total streams, monthly listeners, and track popularity.
- **See how artist contributions differ** when they’re the lead vs. a featured artist.
- **Track how listener behavior and music releases change over time.**
- **Explore the broader music scene** beyond just one artist.

The dashboard is designed for **music industry professionals and fans** who want clear, data-driven insights into how top artists are performing on Spotify.

---

## Data Discovery

<table>
  <tr>
    <th> AIMS GRID</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/geeklakshya/project-img/blob/main/aims%20grid%20spotify.png?raw=true" width="100%">
    </td>
  </tr>
</table>

---

## Data Collection

Due to the lack of sufficient and updated data from a single source, I collected most of the data through web scraping. I used the Spotify API along with BeautifulSoup to scrape data from various platforms. The sources include:

- [Spotify API](https://developer.spotify.com/)
- [Kworb](https://kworb.net/spotify/)
- [Chartmetric](https://chartmetric.com/)
- [Discogs](https://www.discogs.com/)
- [YouTube](https://www.youtube.com/)
- [Google](https://developers.google.com/public-data/docs/canonical/countries_csv)

---

## Data Understanding

After collecting the data, it's crucial to understand the meaning of the dataset — specifically, the significance of each column and what it represents.

- ### Artists_Data.csv (Fact Table)

| Column                     | Type    | Description                                                    |
|----------------------------|---------|----------------------------------------------------------------|
| **artist_name**             | TEXT    | Display name of the artist.                                   |
| **artist_id**               | TEXT    | Unique ID for the artist.                                     |
| **official_name**    | TEXT    | Official/legal name.                                           |
| **type**                    | TEXT    | Individual or group.                                           |
| **gender**                  | TEXT    | Gender identity.                                               |
| **country**                 | TEXT    | Country of origin.                                             |
| **begin_area**              | TEXT    | Region/city of origin.                                         |
| **artist_images**           | TEXT    | URL(s) of artist images.                                       |
| **artist_popularity**       | INTEGER | Popularity score (Spotify metric).                             |
| **artist_followers**        | INTEGER | Number of Spotify followers.                                  |
| **genre_1**                 | TEXT    | Primary genre.                                                 |
| **genre_2**                 | TEXT    | Secondary genre.                                               |
| **d_o_b**                   | DATE    | Date of birth.                                                 |
| **career_debut**    | INTEGER | Year of debut.                                                 |
| **live / deceased / disbanded** | TEXT | Current status.                                                |
| **career end / disband Year** | DECIMAL | Year of disbandment or retirement.                             |


- ### Album_Streams.csv

| Column          | Type    | Description                                                           |
|-----------------|---------|-----------------------------------------------------------------------|
| **Artist ID**   | TEXT    | Unique identifier for the artist (e.g., Spotify artist ID).          |
| **Album Title** | TEXT    | Title of the music album.                                             |
| **Total Streams** | INTEGER | Total number of times the album's tracks have been streamed.         |
| **Daily Streams** | INTEGER | Average number of streams per day.                                    |
| **Spotify URL** | TEXT    | Direct URL to the album on Spotify.                                   |

- ### Artificial_Generated_Daily_Listeners.csv

| Column              | Type    | Description                                                              |
|---------------------|---------|--------------------------------------------------------------------------|
| **Artist**          | TEXT    | Name of the artist.                                                     |
| **Artist ID**       | TEXT    | Unique identifier for the artist.                                       |
| **Monthly Listeners** | INTEGER | Total monthly active listeners (artificially generated estimate).        |
| **Date**            | DATE    | Date of the listener count.                                             |
| **Daily Listeners** | INTEGER   | Estimated listeners per day. |

- ### Artist_Album_Data.csv

| Column            | Type    | Description                                           |
|-------------------|---------|-------------------------------------------------------|
| **album_id**      | TEXT    | Unique identifier for the album.                     |
| **album_titles**  | TEXT    | Name/title of the album.                             |
| **main_artist_id**| TEXT    | ID of the main artist associated with the album.      |
| **main_artist_name** | TEXT | Name of the main artist.                             |
| **album_cover_url** | TEXT  | URL to the album’s cover image.                       |

- ### Artist_Personal_Data.csv

| Column                     | Type    | Description                                                     |
|----------------------------|---------|-----------------------------------------------------------------|
| **artist_name**             | TEXT    | Stage or display name of the artist.                           |
| **artist_id**               | TEXT    | Unique identifier for the artist.                              |
| **official_name**    | TEXT    | Artist's official/legal name.    |
| **type**                    | TEXT    | Whether the artist is a solo act or a group.                   |
| **gender**                  | TEXT    | Gender identity of the artist.                                 |
| **d_o_b**                   | DATE    | Date of birth.                                                 |
| **career_debut**     | INTEGER | Year when the artist's career began.                            |
| **live / deceased / disbanded** | TEXT | Current status: alive, deceased, or disbanded.                 |
| **career end / disband Year** | TEXT   | Year of career end or disbandment (if applicable).             |
| **age**                     | INTEGER | Age of the artist.                                             |
| **genres**                  | TEXT    | Primary genres associated with the artist.                     |

- ### Artist_Spotify_Summary.csv

| Column                     | Type    | Description                                                        |
|----------------------------|---------|--------------------------------------------------------------------|
| **artist_name**             | TEXT    | Name of the artist.                                               |
| **artist_id**               | TEXT    | Unique identifier.                                                |
| **stream_total**            | DECIMAL | Total number of streams across all tracks.                        |
| **stream_as lead**          | INTEGER | Streams where the artist is the lead.                             |
| **stream_solo**             | INTEGER | Streams for solo tracks only.                                     |
| **stream_as feature** (*)   | INTEGER | Streams where the artist is featured.                             |
| **Daily_total**             | INTEGER | Total daily streams across all roles.                             |
| **Daily_as lead**           | INTEGER | Daily streams as lead artist.                                     |
| **Daily_solo**              | INTEGER | Daily solo streams.                                               |
| **Daily_as feature** (*)    | INTEGER | Daily streams as featured artist.                                 |
| **Tracks_total**            | INTEGER | Total number of tracks by the artist.                             |
| **Tracks_as lead**          | INTEGER | Tracks where the artist is the lead.                              |
| **Tracks_solo**             | INTEGER | Solo tracks.                                                      |
| **Tracks_as feature** (*)   | INTEGER | Tracks where the artist is featured.                              |

- ### Avg_Monthly_Listeners.csv

| Column                    | Type    | Description                                                    |
|---------------------------|---------|----------------------------------------------------------------|
| **peak_rank**              | INTEGER | Best rank achieved by the artist.                             |
| **artist_id**              | TEXT    | Unique artist ID.                                             |
| **artist_name**            | TEXT    | Name of the artist.                                           |
| **avg_monthly_listeners**  | INTEGER | Average monthly listener count.                               |
| **daily_avg**              | INTEGER | Daily average listener count.                                 |
| **pk_listeners**           | INTEGER | Listener count at peak rank.                                  |

- ### Songs_Data.csv

| Column                 | Type    | Description                                                   |
|------------------------|---------|---------------------------------------------------------------|
| **album_id**            | TEXT    | Album ID.                                                     |
| **track_id**            | TEXT    | Track ID.                                                     |
| **track_title**         | TEXT    | Original title of the track.                                  |
| **track_title_cleaned** | TEXT    | Cleaned/normalized title.                                     |
| **artist_name**         | TEXT    | Name of the performing artist.                                |
| **artist_id**           | TEXT    | Artist's unique ID.                                           |
| **total_stream**        | INTEGER   | Total streams.                            |
| **daily_avg**           | INTEGER | Average daily streams.                                        |
| **track_duration_mn**   | INTEGER | Track duration in seconds.                                    |
| **ISRC**                | TEXT    | International recording code.                                 |
| **popularity**          | INTEGER | Popularity score.                                             |
| **explicit**            | BOOLEAN | Indicates explicit content.                                   |
| **contributing_artists**| TEXT    | List of contributing artists.                                 |
| **main_artist**         | TEXT    | Main artist name.                                             |
| **ft_artists**          | TEXT    | Featured artists.                                             |
| **track_uri**           | TEXT    | Spotify URI.                                                  |
| **external_url**        | TEXT    | Direct Spotify link.                                          |
| **is_featured**         | BOOLEAN | Indicates if artist is featured.                              |
| **track_duration_min**  | DECIMAL | Track duration in minutes.                                    |
| **type (album/ single)**| TEXT    | Release type.                                                 |
| **album_name**          | TEXT    | Name of the album.                                            |
| **total_tracks**        | INTEGER | Number of tracks in the album.                                |
| **released_date**       | DATE    | Release date of the track.                                    |

- ### YT_Artist.csv

| Column              | Type    | Description                                                       |
|---------------------|---------|-------------------------------------------------------------------|
| **artist_id**       | TEXT    | Unique ID for the artist.                                        |
| **artist_name**     | TEXT    | Artist name.                                                     |
| **yt_usernames**    | TEXT    | Associated YouTube usernames.                                    |
| **total_views**     | INTEGER   | Total views across YouTube channels.         |
| **current_daily_avg** | INTEGER  | Current daily average views.                 |

- ### country_codes.csv

| Column                    | Type    | Description                                                        |
|---------------------------|---------|--------------------------------------------------------------------|
| **country**                | TEXT    | Full name of the country (e.g., "India", "United States").         |
| **alpha-2**                | TEXT    | Two-letter ISO 3166-1 country code (e.g., "IN", "US").            |
| **alpha-3**                | TEXT    | Three-letter ISO 3166-1 country code (e.g., "IND", "USA").        |
| **country-code**           | INTEGER | Numeric ISO 3166-1 country code (e.g., 356 for India).            |
| **iso_3166-2**             | TEXT    | ISO 3166-2 code standard used for identifying subdivisions like states or provinces. |
| **region**                 | TEXT    | Broader geographic region (e.g., "Asia", "Europe").               |
| **sub-region**             | TEXT    | More specific geographic sub-region (e.g., "Southern Asia").      |
| **intermediate-region**    | TEXT    | Optional region level between sub-region and country (blank for many countries). |
| **region-code**            | INTEGER | Numeric code representing the region.                             |
| **sub-region-code**        | INTEGER | Numeric code representing the sub-region.                         |
| **intermediate-region-code** | INTEGER | Numeric code representing the intermediate region (if applicable). |

---

## Data Cleaning and ETL

The data was imported from multiple CSV files into Power BI Desktop. The Power Query Editor was used to perform ETL (Extract, Transform, Load) operations.

### Key Cleaning Steps:
- Filtered out duplicate records  
- Fixed incorrect column data types  
- Filled missing values where applicable  
- Formatted data for consistency (dates, text casing, etc.)  
- Removed unnecessary columns and standardized column names  

---

## Data Modeling

A multi-level star schema was created in Power BI to make the data model fast, easy to use, and scalable.

### Table Classification

| Table Type         | Tables Used                                                                 |
|--------------------|------------------------------------------------------------------------------|
| **Fact Table**     | `Artists_Data`                                                               |
| **Dimension Tables** | `Songs_Data`, `Album_Data`, `YT_Artist`, `Artist_Spotify_Summary`, `Avg_Monthly_Listeners`, `Artist_Persona_Data`, `Album_Stream`, `Dates`, `country_codes`, `Artificial_Generated`|
| **Base Measure Tables** | `Base Measure Pages` (1 & 2) |

### Final Data Model:

<table>
  <tr>
    <th> DATA MODEL</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/geeklakshya/project-img/blob/main/relation.png?raw=true" width="100%">
    </td>
  </tr>
</table>

---
