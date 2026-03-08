import React, { useState, useEffect } from 'react';
import CharacterInfo from './CharacterInfo';

const DebugPage: React.FC = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [characterData, setCharacterData] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Check if user is already logged in
  useEffect(() => {
    const token = localStorage.getItem('eve_access_token');
    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  const handleFetchCharacterData = async () => {
    setLoading(true);
    setError(null);
    
    try {
      // In a real implementation, we would fetch the character ID from the backend
      // and then query ESI API with our access token
      
      // Mock response - this would be replaced by actual backend calls
      const mockCharacterData = {
        character_id: 123456789,
        name: "Test Pilot",
        race_id: 1,
        bloodline_id: 1,
        ancestry_id: 1,
        gender: "male",
        corporation_id: 987654321,
        alliance_id: null,
        security_status: 0.5
      };
      
      setCharacterData(mockCharacterData);
      setLoading(false);
    } catch (err) {
      setError("Failed to fetch character information");
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('eve_access_token');
    setIsLoggedIn(false);
    setCharacterData(null);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>EVE Online Debug Information</h1>
      
      {!isLoggedIn ? (
        <div>
          <p>Please log in with EVE Online to view character information.</p>
          {/* The login button would be here if we implemented it in the current component */}
        </div>
      ) : (
        <div>
          <button 
            onClick={handleFetchCharacterData}
            disabled={loading}
            style={{
              backgroundColor: '#1a2a4d',
              color: 'white',
              border: 'none',
              padding: '8px 16px',
              borderRadius: '4px',
              cursor: 'pointer',
              marginBottom: '20px'
            }}
          >
            {loading ? 'Loading...' : 'Fetch Character Data'}
          </button>
          
          {error && <div style={{ color: 'red' }}>{error}</div>}
          
          {characterData && (
            <CharacterInfo character={characterData} />
          )}
          
          <div style={{ marginTop: '20px' }}>
            <button 
              onClick={handleLogout}
              style={{
                backgroundColor: '#ff4d4d',
                color: 'white',
                border: 'none',
                padding: '8px 16px',
                borderRadius: '4px',
                cursor: 'pointer'
              }}
            >
              Logout
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default DebugPage;