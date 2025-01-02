import "./UseState.css";
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);





  const incrementTwice = () => {
    setCount(count + 1);
    setCount(count + 1);
  };
  // console.log("did i run");

  return (
    <div>
      <p>Count!!: {count}</p>
      <button onClick={incrementTwice}>Increment IM FROM COUNTER</button>
    </div>
  );
}

const ThemeAndCount = () => {
  const [theme, setTheme] = useState("light");

  const [count, setCount] = useState(1);

  return (
    <div className={`state ${theme}`}>
      <h1>UseState Component</h1>

      <Counter />

      {/* <h2>{count}</h2> */}
      {/* <button onClick={() => setCount((prevCount) => prevCount + 1)}>
        Increment
      </button> */}
    </div>
  );
};

export default ThemeAndCount;
