import { useState } from 'react';
import { useHoro } from '../context/HoroscopeContext';

export default function Match() {
    const { sign } = useHoro();
    const [match, setMatch] = useState(false);

    console.log(sign);

    return (
        <>
            <button onClick={() => setMatch(!match)}> Display Match </button>
            {match && <div>{sign.match}</div>}
        </>
    );
}
