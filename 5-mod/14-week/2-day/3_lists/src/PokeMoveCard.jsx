import './PokeMoveCard.css';

// export default function PokeMoveCard(props) {
//     const id = props.id;
//     const type = props.type;
//     const move = props.move;
//     const level = props.level;

export default function PokeMoveCard({ id, type, move, level }) {
    // const id = props.id;
    // const type = props.type;
    // const move = props.move;
    // const level = props.level;

    // const { id, type, move, level } = props;

    return (
        <li className="poke-move-card">
            <h3>Move {id}</h3>
            <h4 style={{ padding: 10 }}>{move.toUpperCase()}</h4>
            <p>Type: {type}</p>
            <p>Level: {level}</p>
        </li>
    );
}
