import React from "react";
import "./viewing.css";
import axios from "axios";
import { useEffect, useState } from "react";

function Viewing() {
  const toEmbedUrl = (url) => {
    const videoIdMatch = url.match(/[?&]v=([^&]+)/);
    const id = videoIdMatch ? videoIdMatch[1] : "";
    return `https://www.youtube.com/embed/${id}`;
  };

  const [videos, setVideos] = useState([]);
  const [query, setQuery] = useState("");
  const [searched, setSearched] = useState(false);

  const handleSearch = () => {
    if (!query.trim()) return;
    axios
      .get(`http://127.0.0.1:5000/api/${encodeURIComponent(query)}`)
      .then((response) => {
        setVideos(response.data);
        setSearched(true);
      })
      .catch((error) => {
        console.error("Error fetching videos:", error);
        setSearched(true);
      });
  };

  return (
    <div className="p-4 space-y-8">
      <div className="search-wrapper">
        <label htmlFor="video-search" className="sr-only">
          Search videos
        </label>
        <input
          id="video-search"
          type="text"
          placeholder="Search videos…"
          className="search-input"
          aria-label="Search videos"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <div className="asdad">
          <button
            className="search-icon"
            aria-hidden="true"
            onClick={handleSearch}
          >
            <i className="fas fa-search"></i>
          </button>
        </div>
      </div>

      {!searched && (
        <p className="text-center text-white text-lg">Search to get results</p>
      )}

      {videos.map((video) => (
        <div key={video.id} className="max-w-xl mx-auto">
          <h3 className="text-lg font-semibold mb-2">{video.name}</h3>
          <div className="aspect-w-16 aspect-h-9 video-wrapper">
            <iframe
              src={toEmbedUrl(video.url)}
              title={video.name}
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
              className="fram"
            />
            <div className="arrow-container" onClick={() => alert(video.url)}>
              <span className="green-arrow">→</span>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Viewing;
