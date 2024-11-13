import React, { useEffect, useState } from 'react';

function BookList() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch('/api/library/books/')
      .then(response => response.json())
      .then(data => setBooks(data));
  }, []);

  return (
    <div>
      <h1>Моя библиотека</h1>
      <ul>
        {books.map(book => (
          <li key={book.id}>{book.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default BookList;
