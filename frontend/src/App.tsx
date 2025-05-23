import React, { useEffect } from 'react';
import { v4 as uuidv4 } from 'uuid';

function send(feature: string) {
  let user = localStorage.getItem('user_id');
  if (!user) {
    user = uuidv4();
    localStorage.setItem('user_id', user);
  }
  fetch('/api/clicks', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ feature_name: feature, user_id: user, timestamp: new Date().toISOString() })
  });
}

const App: React.FC = () => {
  return (
    <div>
      <h1>Feature Analytics Dashboard</h1>
      <button onClick={() => send('feature_a')}>Feature A</button>
      <button onClick={() => send('feature_b')}>Feature B</button>
    </div>
  );
};

export default App;
