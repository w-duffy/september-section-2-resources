import { useState, useEffect } from 'react';
import FunctionComponentTwo from './FunctionComponentTwo';

const FunctionComponentOne = () => {
  const [count, setCount] = useState(0);
  const [message, setMessage] = useState('');

  useEffect(() => {
    setMessage('Hello from useEffect');
  }, []);

  return (
    <div className='center'>
      <h1>Function Component One</h1>
      <div className='one'>
        <button onClick={() => setCount(prevCount => prevCount - 1)}>
          Decrement
        </button>
        <button onClick={() => setCount(prevCount => prevCount + 1)}>
          Increment
        </button>

        <input
          type='text'
          value={message}
          onChange={e => setMessage(e.target.value)}
          placeholder='Enter Your Message'
        />
        <button onClick={() => setMessage('')}>Clear</button>
      </div>

      <FunctionComponentTwo count={count} message={message} />
    </div>
  );
};

export default FunctionComponentOne;
