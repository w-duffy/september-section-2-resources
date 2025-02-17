// import { NavLink } from "react-router-dom";
// import ProfileButton from "./ProfileButton";
// import "./Navigation.css";

// function Navigation() {
//   return (
//     <ul>
//       <li>
//         <NavLink to="/">Home</NavLink>
//       </li>
//       <li>
//         <NavLink to="/images">Images</NavLink>
//       </li>
//       <li>
//         <ProfileButton />
//       </li>
//     </ul>
//   );
// }

// export default Navigation;
// import { NavLink } from "react-router-dom";
// import ProfileButton from "./ProfileButton";
// import "./Navigation.css";

// function Navigation() {
//   return (
//     <nav className="navigation">
//       <div className="nav-container">
//         <div className="logo">
//           <NavLink to="/">MyApp</NavLink>
//         </div>
//         <ul className="nav-links">
//           <li>
//             <NavLink exact to="/" activeClassName="active">
//               Home
//             </NavLink>
//           </li>
//           <li>
//             <NavLink to="/images" activeClassName="active">
//               Images
//             </NavLink>
//           </li>
//         </ul>
//         <div className="profile-section">
//           <ProfileButton />
//         </div>
//       </div>
//     </nav>
//   );
// }

// export default Navigation;

import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import { useState } from "react";

function Navigation() {
  const [isMobile, setIsMobile] = useState(false);

  const handleMenuToggle = () => {
    setIsMobile(!isMobile);
  };

  return (
    <nav className="navigation">
      <div className="nav-container">
        <div className="logo">
          <NavLink to="/">MyApp</NavLink>
        </div>
        <ul className={`nav-links ${isMobile ? "active" : ""}`}>
          <li>
            <NavLink exact to="/" activeClassName="active" onClick={() => setIsMobile(false)}>
              Home
            </NavLink>
          </li>
          <li>
            <NavLink to="/images" activeClassName="active" onClick={() => setIsMobile(false)}>
              Images
            </NavLink>
          </li>
        </ul>
        <div className="profile-section">
          <ProfileButton />
        </div>
        <div className="mobile-menu-icon" onClick={handleMenuToggle}>
          {isMobile ? <>&#10005;</> : <>&#9776;</>}
        </div>
      </div>
    </nav>
  );
}

export default Navigation;
