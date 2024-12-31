import Navigation from "../Navigation";


function Home() {
  console.log("IM ON THE CLIENT")
  return (
    <div className="comp orange">
      <Navigation />
      <h1>Home Component</h1>
    </div>
  );
}

export default Home;
