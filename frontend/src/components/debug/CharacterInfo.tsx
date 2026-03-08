import React from 'react';

interface CharacterData {
  character_id: number;
  name: string;
  race_id: number;
  bloodline_id: number;
  ancestry_id: number;
  gender: string;
  corporation_id: number;
  alliance_id: number | null;
  security_status: number;
}

interface CharacterInfoProps {
  character?: CharacterData;
  loading?: boolean;
  error?: string;
}

const CharacterInfo: React.FC<CharacterInfoProps> = ({ character, loading, error }) => {
  if (loading) {
    return <div className="character-info">Loading character information...</div>;
  }

  if (error) {
    return <div className="character-info error">{error}</div>;
  }

  if (!character) {
    return <div className="character-info">No character data available</div>;
  }

  return (
    <div className="character-info">
      <h2>Character Information</h2>
      
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: '1fr 1fr', 
        gap: '16px',
        backgroundColor: '#f5f5f5',
        padding: '16px',
        borderRadius: '8px'
      }}>
        <div>
          <h3>Basic Info</h3>
          <p><strong>Name:</strong> {character.name}</p>
          <p><strong>ID:</strong> {character.character_id}</p>
          <p><strong>Gender:</strong> {character.gender}</p>
          <p><strong>Security Status:</strong> {character.security_status}</p>
        </div>
        <div>
          <h3>Organization</h3>
          <p><strong>Corporation ID:</strong> {character.corporation_id}</p>
          <p><strong>Alliance ID:</strong> {character.alliance_id || 'None'}</p>
          <p><strong>Race:</strong> {character.race_id}</p>
        </div>
      </div>
    </div>
  );
};

export default CharacterInfo;