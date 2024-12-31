import Showcase from './Showcase';
import './App.css';
import BaseStats from './BaseStats';
// https://stackblitz.com/github/w-duffy/september-section-2-resources/tree/main/5-mod/14-week/2-day/2_props

function App() {
    const baseStats = {
        hp: 45,
        attack: 49,
        defense: 49,
        spAttack: 65,
        spDef: 65,
        speed: 45,
    };

    const handleClick = () =>
        alert(
            `Special Stats\n\tSpecial Attack: ${baseStats.spAttack}\n\tSpecial Defense: ${baseStats.spDef}`
        );

// fetch("/api/spots")
// [{spotId: 1, location: "texas"}, {spotId: 2, location: "california"}]
// [{reviewId: 1, text: "Cool!"}, {reviewId: 2, text: "great Spot!"}]
    return (
        <div className="main-wrapper background">
            <Showcase pokemonName="bulbasaur" />
            <BaseStats stats={baseStats} clicker={handleClick}/>
            {/* <Showcase pokemonImage="charmernaderImageUrl" pokemonName="charmander" />
            <Showcase pokemonImage="charmernaderImageUrl" pokemonName="pika" />
            <Showcase pokemonImage="charmernaderImageUrl" pokemonName="squirt" />
 */}

            {/* <BaseStats {...baseStats} /> */}
            {
                // <BaseStats hp={baseStats.hp} attack={49} etc... />
            }
        </div>
    );
}

export default App;
