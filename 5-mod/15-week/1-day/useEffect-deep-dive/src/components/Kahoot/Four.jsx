import { useEffect, useState } from 'react';

export default function KahootFour() {
    const [num, setNum] = useState(0);

    console.log(
        '----------------------Component rerendered----------------------',
        num
    );

    useEffect(() => {
        console.log('useEffect main function:', num);

        return () => console.log('useEffect CLEANUP FUNCTION:', num);
    }, [num]);

    useEffect(() => {
        console.log('lonely effect main', num);

        return () => console.log('lonely effect CLEANUP FUNCTION:', num);
    }, []);

    return (
        <div>
            <h1>{num}</h1>
            <button onClick={() => setNum((prevNum) => prevNum + 1)}>
                Increment
            </button>
            <button onClick={() => setNum((prevNum) => prevNum - 1)}>
                Decrement
            </button>
        </div>
    );
}
