import { moves } from "./data.js";
import PokeMoveCard from "./PokeMoveCard.jsx";
import './PokeMoveCard.css';
export default function PokeMoves() {
  console.log("moves", moves);
  // fetch('/api/spots')


  return (
    <div>
      <h1> PokeMoves </h1>
      <ul>
        {moves.map((el) =>(
                    <PokeMoveCard key={el.id} {...el} />
                ))}

      </ul>
    </div>
  );
}
