import './BaseStats.css';

// export default function BaseStats(props) { //? props variable
//     const stats = props.stats; //? then access stats
//     const clicker = props.clicker; //? then access clicker

// export default function BaseStats({ stats, clicker }) { //! destructure props
//     const { hp, attack, defense, speed } = stats; //! then destructure stats

// export default function BaseStats({
//     stats: { hp, attack, defense, speed },
//     clicker,
// }) {

export default function BaseStats(taco) {
    const { hp, attack, defense, speed } = taco.stats;
    const clicker = taco.clicker;
    //* Do all destructuring at once!
    return (
        <div className="base-stats">
            <h1>Base Stats</h1>
            {/* <button onClick={() => clicker()} className="sp-stats">
                Check Special Stats
            </button> */}
            <button onClick={clicker} className="sp-stats">
                Check Special Stats
            </button>
            <table>
                <tbody>
                    <tr>
                        <td>Hit Points</td>
                        <td>{hp}</td>
                    </tr>
                    <tr>
                        <td>Attack</td>
                        <td>{attack}</td>
                    </tr>
                    <tr>
                        <td>Defense</td>
                        <td>{defense}</td>
                    </tr>
                    <tr>
                        <td>Speed</td>
                        <td>{speed}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
}
