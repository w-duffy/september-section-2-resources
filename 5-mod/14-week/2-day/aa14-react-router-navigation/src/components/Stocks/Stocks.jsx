import { Navigate, useNavigate } from 'react-router-dom';

function Stocks() {
  const navigate = useNavigate();

  const loggedIn = true;

  const handleClick = () => {
      window.alert('Fake GET request; getting data from Ohio DB!');
      navigate('/');
  };

  if (!loggedIn) return <Navigate to="/not-logged-in" />;

  return (
      <div className="comp orange">
          <h1 style={{color: "red"}}>stocks Component</h1>
          <button onClick={handleClick}>Buy the DIP! 📈</button>
      </div>
  );
}

export default Stocks
