import { useEffect, useState } from 'react';

//! COMMENT OUT <StrictMode> IN APP.JSX IF YOU WANT THIS TO WORK!!!!
//! COMMENT OUT <StrictMode> IN APP.JSX IF YOU WANT THIS TO WORK!!!!
//! COMMENT OUT <StrictMode> IN APP.JSX IF YOU WANT THIS TO WORK!!!!
//! COMMENT OUT <StrictMode> IN APP.JSX IF YOU WANT THIS TO WORK!!!!
//! COMMENT OUT <StrictMode> IN APP.JSX IF YOU WANT THIS TO WORK!!!!
//! COMMENT OUT <StrictMode> IN APP.JSX IF YOU WANT THIS TO WORK!!!!

export default function KahootTwo() {
    console.log('Component just rerendered');

    const [storageItem, setStorageItem] = useState('Default value');

    useEffect(() => {
        console.log('First useEffect just ran', storageItem);

        const val = localStorage.getItem('nameOfThirdCat');
        setStorageItem(val || 'Default value');

        return () => console.log('First effect unmounted!');
    }, []);

    useEffect(() => {
        console.log('Second useEffect ran just now!!!!', storageItem);
        localStorage.setItem('nameOfThirdCat', 'Kiki');

        return () => console.log('SECOND effect unmounted!!!');
    }, [storageItem]);

    return (
        <div>
            <input
                type="text"
                value={storageItem}
                onChange={(e) => setStorageItem(e.target.value)}
            />
            <h1>{storageItem}</h1>
        </div>
    );
}
