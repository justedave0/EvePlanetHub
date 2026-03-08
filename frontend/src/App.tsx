import React, { useState, useEffect } from 'react';
import EVELoginButton from './components/auth/EVELoginButton';
import DebugPage from './components/debug/DebugPage';
import './App.css';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Check if user is already logged in (check for token or session)
  useEffect(() => {
    // This would typically check for valid auth token in local storage or cookies 
    const token = localStorage.getItem('eve_access_token');
    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to EvePlanetHub</h1>
        <p>React frontend with TypeScript</p>
        
        {!isLoggedIn ? (
          <div style={{ marginTop: '20px' }}>
            <h2>Login with EVE Online</h2>
            <EVELoginButton />
          </div>
        ) : (
          <div>
            <DebugPage />
          </div>
        )}
      </header>
    </div>
  );
}

export default App;