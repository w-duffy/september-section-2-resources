import horoscopesObj from '../data/horoscopes';
import { useHoro } from '../context/HoroscopeContext';

const Navbar = () => {
    const { setCurrentSign } = useHoro();
    const horoscopes = Object.keys(horoscopesObj);

    return (
        <nav>
            {horoscopes.map((sign) => (
                <span key={sign} onClick={() => setCurrentSign(sign)}>
                    {sign}
                </span>
            ))}
        </nav>
    );
};

export default Navbar;
