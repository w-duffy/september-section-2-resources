import Showcase from './Showcase';
import './App.css';
import BaseStats from './BaseStats';

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

    return (
        <div className="main-wrapper background">
            <Showcase />
            <BaseStats stats={baseStats} clicker={handleClick} />
            {/* <BaseStats {...baseStats} /> */}
            {
                // <BaseStats hp={baseStats.hp} attack={49} etc... />
            }
        </div>
    );
}

export default App;
