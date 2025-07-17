import { useState } from 'react';

const App = () => {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setResponse('');

    try {
      const res = await fetch('https://asystent-backend-k5kz.onrender.com/api/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      });

      const data = await res.json();
      setResponse(data.result || 'Brak odpowiedzi.');
    } catch (err) {
      setResponse('Błąd połączenia z serwerem.');
    }

    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: '0 auto', padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Asystent Zakupowy</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={query}
          onChange={e => setQuery(e.target.value)}
          placeholder="Czego szukasz?"
          style={{ width: '100%', padding: '0.5rem', fontSize: '1rem' }}
          required
        />
        <button type="submit" style={{ marginTop: '1rem', padding: '0.5rem 1rem' }}>
          Szukaj
        </button>
      </form>
      <div style={{ marginTop: '2rem', whiteSpace: 'pre-wrap' }}>
        {loading ? 'Szukam...' : response}
      </div>
    </div>
  );
};

export default App;
