import { moves } from './data.js';
import PokeMoveCard from './PokeMoveCard.jsx';

export default function PokeMoves() {
    return (
        <div>
            <h1> PokeMoves </h1>
            <ul>
                {moves.map((el) => (
                    <PokeMoveCard key={el.id} {...el} />
                ))}
                {moves.map(({ id, move, ...el }) => (
                    // <li key={id}>
                    //     {id}. {move}
                    // </li>
                    <PokeMoveCard key={id} id={id} move={move} {...el} />
                ))}
            </ul>
        </div>
    );
}
