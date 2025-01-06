import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

// let pretendRedux;

export default function Kahoot() {
    const [kahootImages, setKahootImages] = useState([]);

    useEffect(() => {
        const getKahootImages = async () => {
            const check = await fetch('http://localhost:3000/api/kahoots');
            const checkRes = await check.json();
            setKahootImages(checkRes.imageURLs);
            // pretendRedux = checkRes.imageURLs;
        };

        getKahootImages();

    }, []);

    return (
        <div>
            <h2>Kahoot Home</h2>
            <div
                style={{
                    display: 'flex',
                    maxWidth: '100vw',
                    justifyContent: 'space-around',
                    flexWrap: 'wrap',
                }}
            >
                {/*
                    Does kahootImages have images?
                    If yes, use that
                    If no, in the mean time, use pretendRedux
                */}
                {kahootImages.map((el, i) => {
                    return (
                        <Link key={i} to={`${i + 1}`}>
                            <img src={el} alt={`Kahoot #${i + 1}`} />
                        </Link>
                    );
                })}
            </div>
        </div>
    );
}

// const kahootImages = [
//     <img
//         key={'61f18b15'}
//         src="https://images-cdn.kahoot.it/61f18b15-fc9c-45e9-baab-0d402ede662f?auto=webp"
//         width={500}
//     />,
//     <img
//         key={'e788f11a'}
//         width={500}
//         src="https://images-cdn.kahoot.it/e788f11a-7f13-4be8-ace3-79b241a5e48d?auto=webp"
//     />,
//     <img
//         key={'619bbd46'}
//         width={500}
//         src="https://images-cdn.kahoot.it/619bbd46-d42a-4f95-88fd-0b227e691550?auto=webp"
//     />,
//     <img
//         key={'91cd0c5c'}
//         width={500}
//         src="https://images-cdn.kahoot.it/91cd0c5c-bb2e-4875-a3ba-27f693969247?auto=webp"
//     />,
// ];

// export default function Kahoot() {

//     return (
//         <div>
//             <h2>Kahoot Home</h2>
//             <div
//                 style={{
//                     display: 'flex',
//                     width: '100vw',
//                     justifyContent: 'space-around',
//                     flexWrap: 'wrap',
//                 }}
//             >
//                 {kahootImages.map((el, i) => {
//                     return (
//                         <Link key={el.key} to={`${i + 1}`}>
//                             {el}
//                         </Link>
//                     );
//                 })}
//             </div>
//         </div>
//     );
// }
