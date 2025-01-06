import { NavLink } from 'react-router-dom';

export default function NavBar() {
    return (
        <nav style={{ position: 'absolute', top: 0, left: 0, width: '100vw' }}>
            <ul
                style={{
                    display: 'flex',
                    justifyContent: 'space-evenly',
                    fontSize: '2rem',
                }}
            >
                <li>
                    <NavLink style={{ padding: '0.3rem' }} to="/">
                        Home
                    </NavLink>
                </li>
                <li>
                    <NavLink style={{ padding: '0.3rem' }} to="/function">
                        Function
                    </NavLink>
                </li>
                <li>
                    <NavLink style={{ padding: '0.3rem' }} to="/class">
                        Class
                    </NavLink>
                </li>
                <li>
                    <NavLink style={{ padding: '0.3rem' }} to="/kahoot">
                        Kahoot
                    </NavLink>
                </li>
            </ul>
        </nav>
    );
}
