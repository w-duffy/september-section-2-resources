import { Outlet } from "react-router-dom";
function Home() {
  return (
    <div className="comp orange">
      <h1>Home Component</h1>
      <Outlet />
    </div>
  );
}

export default Home;
