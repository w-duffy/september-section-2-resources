import BulbaPic from './images/bulbasaur.jpg';

export default function Showcase() {
    const favPokemon = 'Bulbasaur';

    const pokeCharacteristics = {
        type: 'Grass',
        move: 'Solar Beam',
    };

    return (
        <div>
            <h1>{`${favPokemon}'s Showcase Component`}</h1>
            {console.log("HERE!")}
            {/* <h1>{favPokemon}&apos;s Showcase Component</h1> */}
            <img src={BulbaPic} alt={favPokemon} width={300}/>
            <h2>
                {`${favPokemon}'s`} type is
                <span style={{ backgroundColor: 'green', color: 'white' }}>
                    {pokeCharacteristics.type}
                </span>
                , and one of their moves is{' '}
                <span style={{ backgroundColor: '#FFFFFF', color: '#00FF00' }}>
                    {pokeCharacteristics.move}
                </span>
            </h2>
        </div>
    );
}

export const myOtherComp = () => <div></div>;

// const Showcase = () => {
//     return (
//         <div>
//             <h1>Showcase Component</h1>
//         </div>
//     );
// };

// export default Showcase;
