import { useEffect, useState } from 'react';

export default function KahootOne({ value }) {
    const [count, setCount] = useState(0);

    useEffect(() => {
        // setCount((prevCount) => prevCount + 1);
        setCount(count + 1);
        console.log('Hey look at me', count);
    }, [value]);

    return (
        <div>
            <h1>{count}</h1>
            <button>Click</button>
        </div>
    );
}
