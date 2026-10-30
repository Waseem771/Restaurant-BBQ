import React, { lazy, Suspense, useEffect, useState } from 'react';
import { SettingsProvider, useSettings } from './context/SettingsContext';
import LoginPage from './components/LoginPage';
import authService from './services/authService';
import './App.css';

/** True when a JWT is missing, malformed, or past its `exp` claim. */
function isTokenExpired(token) {
  try {
    const payload = JSON.parse(atob(token.split('.')[1].replace(/-/g, '+').replace(/_/g, '/')));
    return !payload.exp || payload.exp * 1000 <= Date.now();
  } catch {
    return true;
  }
}

// Charts and AI UI load only after a successful sign-in.
const Dashboard = lazy(() => import('./components/Dashboard'));

/**
 * Inner App Component
 * Wrapped by SettingsProvider for access to settings context
 */
function AppContent() {
  const { config, settings, setTheme } = useSettings();
  const [user, setUser] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  // Initialize theme on mount
  useEffect(() => {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const savedTheme = localStorage.getItem('bbq_theme');
    const theme = savedTheme || (prefersDark ? 'dark' : 'light');

    setTheme(theme);
    document.documentElement.setAttribute('data-theme', theme);
  }, [setTheme]);

  // Check for existing session
  useEffect(() => {
    const sessionData = localStorage.getItem('bbq_user_session') ||
                       sessionStorage.getItem('bbq_user_session');

    if (sessionData) {
      try {
        const parsedSession = JSON.parse(sessionData);
        if (isTokenExpired(parsedSession.token)) {
          // Stale session: every API call would fail and the dashboard would
          // show empty "—" values. Send the user back to the login screen.
          authService.logout();
        } else {
          setUser(parsedSession);
        }
      } catch (err) {
        console.error('Failed to parse session:', err);
        localStorage.removeItem('bbq_user_session');
      }
    }

    setIsLoading(false);
  }, []);

  // Apply global styles based on settings
  useEffect(() => {
    const root = document.documentElement;

    // Set CSS variables for colors
    root.style.setProperty('--color-primary', config.COLORS.primary);
    root.style.setProperty('--color-secondary', config.COLORS.secondary);
    root.style.setProperty('--color-success', config.COLORS.success);
    root.style.setProperty('--color-warning', config.COLORS.warning);
    root.style.setProperty('--color-error', config.COLORS.error);
    // Surface, background and text colours come from the light/dark theme in
    // App.css. Forcing the dark config values here made cards dark while the
    // text stayed dark (light theme), so headings and values were unreadable.
    for (const v of ['--color-background', '--color-surface', '--color-text']) {
      root.style.removeProperty(v);
    }

    // Set typography
    root.style.setProperty('--font-family-default', config.TYPOGRAPHY.fontFamily.default);
    root.style.setProperty('--font-family-mono', config.TYPOGRAPHY.fontFamily.mono);

    // Set transition duration
    root.style.setProperty('--transition-duration', `${config.UI.transitionDuration}ms`);
  }, [config]);

  // Log debug info if enabled
  useEffect(() => {
    if (config.DEBUG.enabled) {
      console.log('🎨 BBQ Dashboard Initialized');
      console.log('Configuration:', config);
      console.log('Settings:', settings);
      console.log('Theme:', settings.theme);
      console.log('User:', user);
    }
  }, [config, settings, user]);

  // api.js fires this when the backend rejects the token (401).
  useEffect(() => {
    const onExpired = () => { authService.logout(); setUser(null); };
    window.addEventListener('bbq:auth-expired', onExpired);
    return () => window.removeEventListener('bbq:auth-expired', onExpired);
  }, []);

  const handleLoginSuccess = (sessionData) => {
    setUser(sessionData);
    if (config.DEBUG.enabled) {
      console.log('✅ User logged in:', sessionData.email);
    }
  };

  const handleLogout = () => {
    authService.logout();
    setUser(null);

    if (config.DEBUG.enabled) {
      console.log('🚪 User logged out');
    }
  };

  if (isLoading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <div className="app-container" data-theme={settings.theme}>
      {user ? (
        <Suspense fallback={<div className="loading-container"><div className="loading-spinner" /><p>Loading dashboard...</p></div>}>
          <Dashboard user={user} onLogout={handleLogout} />
        </Suspense>
      ) : (
        <LoginPage onLoginSuccess={handleLoginSuccess} />
      )}
    </div>
  );
}

/**
 * Root App Component
 * Provides settings context to entire application
 */
export default function App() {
  return (
    <SettingsProvider>
      <AppContent />
    </SettingsProvider>
  );
}
