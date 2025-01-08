const initialState = [{ 1: 'banana', 2: 'pear', 3: 'orange', 4: 'peach' }];

const FRUIT_KILLA = 'kill/it/all';

export const fruitKilla = () => {
    return {
        type: FRUIT_KILLA,
    };
};

const fruitReducer = (state = initialState, action) => {
    // console.log("HEY LOOK I'M THE FRUIT REDUCER");

    switch (action.type) {
        case FRUIT_KILLA:
            return [];

        default:
            return state;
    }
};

export default fruitReducer;
