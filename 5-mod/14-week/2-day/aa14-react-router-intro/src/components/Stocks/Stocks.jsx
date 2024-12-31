// import Navigation from "../Navigation";
function Navigation(){
  return (
    <nav>
      <ul>
        <li><a href='/'>Home</a></li>
        <li><a href='/stocks'>Stocks</a></li>
        <li><a href='/movies'>Movies</a></li>
      </ul>
    </nav>
  )
}

function Stocks() {
  return (
    <div className='comp orange'>
      <Navigation />
      <h1>Stocks Component</h1>
      <p>I render at /stocks</p>
    </div>
  );
}

export default Stocks;
