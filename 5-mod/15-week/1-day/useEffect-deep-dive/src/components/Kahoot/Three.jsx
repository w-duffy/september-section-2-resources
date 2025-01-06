import { useEffect, useState } from 'react';

export default function KahootThree() {
    console.log('-------------Component just rerendered!------------------');

    const [color, setColor] = useState('blue');
    const [count, setCount] = useState(65);

    useEffect(() => {
        console.log('First useEffect is running');
        console.log('Color', color);
        console.log('Count', count);

        if (count > 50) {
            setColor('red');
        } else {
            setColor('green');
        }
    }, [count]);

    useEffect(() => {
        console.log('SECOND useEFFECT IS RUNNING!!!!!');
        console.log('Color', color);
        console.log('Count', count);
        if (color === 'blue') {
            setCount(0);
        }
    }, [color]);

    return (
        <div>
            <h1>Count: {count}</h1>
            <h1>Color: {color}</h1>
        </div>
    );
}
