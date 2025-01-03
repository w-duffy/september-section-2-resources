import { createContext, useContext, useState } from 'react';
import horoscopesObj from '../data/horoscopes';

export const HoroscopeContext = createContext();

export const useHoro = () => useContext(HoroscopeContext)

const HoroscopeProvider = ({children}) => {
  const [currentSign, setCurrentSign] = useState('Leo');
  const sign = horoscopesObj[currentSign];

  return (
    <HoroscopeContext.Provider value={{ sign, setCurrentSign }}>
      {children}
    </HoroscopeContext.Provider>
  );
};


export default HoroscopeProvider;
