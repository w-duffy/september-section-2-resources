import { Component } from 'react';
// let instance = new ClassComponent()

class ClassComponent extends Component {
    constructor(props) {
        super(props);
        console.log("Hey I'm in the constructor");
        this.state = {
            seconds: 0,
            ten: false,
        };
    }

    componentDidMount() {
        console.log("I'm running and I'm mountin");

        // this.timer = setInterval(() => {
        //     this.setState((prevState) => {
        //         return {
        //             seconds: prevState.seconds + 1,
        //         };
        //     });
        // }, 5000);
    }

    componentDidUpdate(prevProps, prevState) {
        if (prevState.seconds !== this.state.seconds) {
            console.log('Did things update?');
            if (this.state.seconds >= 10) {
                this.setState({
                    ten: true,
                });
            }
        }
    }

    componentWillUnmount() {
        console.log('Component successfully unmounted!');
        clearInterval(this.timer);
    }

    render() {
        console.log('I just rendered, maybe even re-rendered!');

        // console.log(this);

        return (
            <div>
                <h2>{this.state.seconds} seconds have passed</h2>
                <button
                    onClick={() =>
                        this.setState((prevState) => {
                            return {
                                seconds: prevState.seconds + 1,
                            };
                        })
                    }
                >
                    +1 second
                </button>
                {this.state.ten && (
                    <h2>{"You've"} been here longer than 10 seconds!</h2>
                )}
            </div>
        );
    }
}

export default ClassComponent;
