// src/App.js
import React, { useState, useEffect } from 'react';
import './App.css';

const GOOGLE_CLIENT_ID = '865209583510-ncomqfrmdd3b5jma73kn3id5hk8e1894.apps.googleusercontent.com';
const DJANGO_API_URL = 'http://localhost:8000/api'; // Correct

function App() {
  const [user, setUser] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Check if user is already logged in
    const token = localStorage.getItem('access_token');
    if (token) {
      fetchUserProfile(token);
    }

    // Load Google API
    loadGoogleAPI();
  }, []);

  const loadGoogleAPI = () => {
    const script = document.createElement('script');
    script.src = 'https://accounts.google.com/gsi/client';
    script.onload = initializeGoogleSignIn;
    document.body.appendChild(script);
  };

  const initializeGoogleSignIn = () => {
    if (window.google) {
      window.google.accounts.id.initialize({
        client_id: GOOGLE_CLIENT_ID,
        callback: handleGoogleResponse,
      });

      window.google.accounts.id.renderButton(
        document.getElementById('google-signin-button'),
        {
          theme: 'outline',
          size: 'large',
          text: 'signin_with',
          shape: 'rectangular',
        }
      );
    }
  };

  const handleGoogleResponse = async (response) => {
    setIsLoading(true);
    setError(null);

    try {
      // Send ID token to Django backend
      const backendResponse = await fetch(`${DJANGO_API_URL}/google/id-token/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          id_token: response.credential,
        }),
      });

      const data = await backendResponse.json();

      if (backendResponse.ok) {
        setUser(data.user);
        localStorage.setItem('access_token', data.access_token);
        localStorage.setItem('refresh_token', data.refresh_token);
      } else {
        setError(data.error || 'Login failed');
      }
    } catch (err) {
      setError('Network error. Please try again.');
      console.error('Login error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const fetchUserProfile = async (token) => {
    try {
      const response = await fetch(`${DJANGO_API_URL}/profile/`, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setUser(data.user);
      } else {
        // Token might be expired
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
      }
    } catch (err) {
      console.error('Profile fetch error:', err);
    }
  };

  const handleLogout = () => {
    setUser(null);
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    
    if (window.google) {
      window.google.accounts.id.disableAutoSelect();
    }
  };

  return (
    <div className="App">
      <div className="container">
        <h1>Django AllAuth + Google OAuth2</h1>
        
        {error && (
          <div className="error-message">
            {error}
          </div>
        )}
        
        {!user ? (
          <div className="login-section">
            <h2>Please Sign In</h2>
            <p>Sign in with your Google account to continue</p>
            
            {isLoading ? (
              <div className="loading">
                <div className="spinner"></div>
                <p>Signing in...</p>
              </div>
            ) : (
              <div>
                <div id="google-signin-button"></div>
                <p className="instructions">
                  Click the button above to sign in with Google
                </p>
              </div>
            )}
          </div>
        ) : (
          <div className="user-section">
            <h2>Welcome back!</h2>
            <div className="user-card">
              <div className="user-info">
                <p><strong>Name:</strong> {user.name || 'Not provided'}</p>
                <p><strong>Email:</strong> {user.email}</p>
                <p><strong>User ID:</strong> {user.id}</p>
              </div>
              <button 
                className="logout-button" 
                onClick={handleLogout}
              >
                Sign Out
              </button>
            </div>
          </div>
        )}
        
        <div className="footer">
          <p>Make sure Django server is running on localhost:8000</p>
        </div>
      </div>
    </div>
  );
}

export default App;