import BulbaPic from './images/bulbasaur.jpg';

//fetch('/api/spots/{spotId}')
// {Spot: {spotName: 'Spot 1', spotImage: Spot1, spotDescription: 'This is a spot description'}}
function NewComponent(){
    return (
        <h1>Hello World</h1>
    )
}

function MoonComponent(){
    return (
        <h1>Hello Moon</h1>
    )
}

function helloPerson(name){
    return `Hello ${name}`
}
console.log(helloPerson('Will'))


export default function Showcase() {
    const favPokemon = 'Bulbasaur';

    const pokeCharacteristics = {
        type: 'Grass',
        move: 'Solar Beam',
    };

    return (
        <div>
            <NewComponent someProp="someValue" />
            <MoonComponent />
            {console.log("I'm in showcase.jsx")}
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



// const Showcase = () => {
//     return (
//         <div>
//             <h1>Showcase Component</h1>
//         </div>
//     );
// };

// export default Showcase;
