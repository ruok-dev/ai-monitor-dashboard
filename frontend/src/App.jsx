import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [logs, setLogs] = useState([
    { id: 1, timestamp: '2026-04-26 19:20:01', level: 'INFO', service: 'AuthService', message: 'User logged in successfully' },
    { id: 2, timestamp: '2026-04-26 19:20:05', level: 'ERROR', service: 'PaymentAPI', message: 'Transaction timeout at gateway' },
    { id: 3, timestamp: '2026-04-26 19:20:10', level: 'WARNING', service: 'Database', message: 'High connection pool usage' },
  ]);

  return (
    <div className="layout">
      <aside className="sidebar">
        <h1 className="logo">AI Monitor</h1>
        <nav>
          <ul>
            <li className="active">Dashboard</li>
            <li>Logs</li>
            <li>Alerts</li>
            <li>Settings</li>
          </ul>
        </nav>
      </aside>
      
      <main className="main-content">
        <header className="page-header">
          <h2>Overview</h2>
          <div className="user-profile">Admin</div>
        </header>

        <div className="stats-grid">
          <div className="glass-card stat-card">
            <span className="label">Total Logs</span>
            <span className="value">12.4k</span>
            <span className="trend positive">+12% vs last hr</span>
          </div>
          <div className="glass-card stat-card">
            <span className="label">Active Alerts</span>
            <span className="value danger">3</span>
            <span className="trend">Critical status</span>
          </div>
          <div className="glass-card stat-card">
            <span className="label">Anomaly Rate</span>
            <span className="value warning">0.8%</span>
            <span className="trend negative">+2% vs last hr</span>
          </div>
        </div>

        <section className="recent-logs">
          <div className="glass-card">
            <h3>Recent Logs</h3>
            <div className="log-table">
              {logs.map(log => (
                <div key={log.id} className="log-row">
                  <span className="timestamp">{log.timestamp}</span>
                  <span className={`level ${log.level.toLowerCase()}`}>{log.level}</span>
                  <span className="service">{log.service}</span>
                  <span className="message">{log.message}</span>
                </div>
              ))}
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
