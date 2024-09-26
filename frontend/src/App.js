import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Fetch data from FastAPI API endpoint
    fetch("/api/data")
      .then((response) => response.json())
      .then((fetchedData) => {
        setData(fetchedData);
      });
  }, []);

  return (
    <div>
      <h1>{data ? data.message : "Loading..."}</h1>
      {data && data.items && (
        <ul>
          {data.items.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
