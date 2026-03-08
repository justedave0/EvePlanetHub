import React from 'react';

const EVELoginButton: React.FC = () => {
  const handleLogin = () => {
    // Directly redirect to the EVE SSO login endpoint
    window.location.href = '/api/v1/auth/eve/login';
  };

  return (
    <button 
      onClick={handleLogin}
      className="eve-login-button"
      style={{
        backgroundColor: '#1a2a4d',
        color: 'white',
        border: 'none',
        padding: '12px 24px',
        fontSize: '16px',
        borderRadius: '4px',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        gap: '8px',
        textDecoration: 'none'
      }}
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm0 22C6.486 22 2 17.514 2 12S6.486 2 12 2s10 4.486 10 10-4.486 10-10 10z"/>
        <path d="M12 6c-3.314 0-6 2.686-6 6s2.686 6 6 6 6-2.686 6-6-2.686-6-6-6zm0 10c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4z"/>
        <circle cx="12" cy="12" r="2"/>
      </svg>
      Login with EVE Online
    </button>
  );
};

export default EVELoginButton;