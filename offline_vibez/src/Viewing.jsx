import React from 'react';
import './viewing.css'
// Sample data (could be fetched or imported instead)
const videos = [
  {
    id: 1,
    name: "Lil Tecca - Ransom (Official Music Video)",
    url: "https://www.youtube.com/watch?v=1XzY2ij_vL4"
  },
  {
    id: 2,
    name: "Lil Tecca - Ransom (Lyrics)",
    url: "https://www.youtube.com/watch?v=0Cshm-BsiaU"
  },
  {
    id: 3,
    name: "Lil Tecca - Ransom (Lyrics)",
    url: "https://www.youtube.com/watch?v=Sz-zo83cogY"
  },
  {
    id: 4,
    name: "Lil Tecca, Juice WRLD - Ransom (Clean - Lyrics)",
    url: "https://www.youtube.com/watch?v=jvcQwGvh9HQ"
  },
  {
    id: 5,
    name: "Lil Tecca - Ransom (Clean - Lyrics)",
    url: "https://www.youtube.com/watch?v=O0hiTfGicKQ"
  }
];

// Utility to convert a YouTube URL into an embeddable URL
const toEmbedUrl = (url) => {
  const videoIdMatch = url.match(/[?&]v=([^&]+)/);
  const id = videoIdMatch ? videoIdMatch[1] : '';
  return `https://www.youtube.com/embed/${id}`;
};

export default function Viewing() {
  return (
    <div className="p-4 space-y-8">
      {videos.map(video => (
        <div key={video.id} className="max-w-xl mx-auto">
          <h3 className="text-lg font-semibold mb-2">{video.name}</h3>
          <div className="aspect-w-16 aspect-h-9">
            <iframe
              src={toEmbedUrl(video.url)}
              title={video.name}
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
              className="fram"
            />
          </div>
        </div>
      ))}
    </div>
  );
}
