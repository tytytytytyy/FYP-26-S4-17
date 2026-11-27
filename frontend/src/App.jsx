import { useEffect, useState } from 'react'

const API = 'http://localhost:8000'

export default function App() {
  const [status, setStatus] = useState('checking...')

  useEffect(() => {
    fetch(`${API}/health`)
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus('backend not reachable'))
  }, [])

  return (
    <main style={{ fontFamily: 'sans-serif', padding: 24 }}>
      <h1>HITL IDS Dashboard</h1>
      <p>Backend status: {status}</p>
    </main>
  )
}
