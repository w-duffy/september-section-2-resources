// import {createContext, useState, useContext} from 'react';

// let NewContext = createContext();

// let NewContextProvider = ({children}) => {
//     let [someProp, setSomeProp] = useState('I came from context');
//     return (
//         <NewContext.Provider value={someProp}>
//             {children}
//         </NewContext.Provider>
//     );
// };

import { createContext, useState, useContext } from "react";

let NewContext = createContext();

let NewContextProvider = ({ children }) => {
  let [someProp, ] = useState("I came from context");

  return <NewContext.Provider value={someProp}>{children}</NewContext.Provider>;
};

const PropDrillingParent = () => {
  let dynamicValue = "I came from the parent component";
  return (
    <NewContextProvider>
      <PropDrillingChild dynamicValue={dynamicValue} />
    </NewContextProvider>
  );
};

function PropDrillingChild() {
  return <PropDrillingGrandChild />;
}

function PropDrillingGrandChild() {

  return <PropDrillingGreatGrandChild />;
}

function PropDrillingGreatGrandChild() {
    let dynamicValue = useContext(NewContext);
  return (
    <div>
      <h1>Prop Drilling</h1>
      <p>{dynamicValue}</p>
    </div>
  );
}

const SideCard = () => {
  console.log("SideCard rerendered!");

  return (
    <div className="side-card">
      <h1>React Context with Horoscopes</h1>
      <PropDrillingParent />
    </div>
  );
};

export default SideCard;
