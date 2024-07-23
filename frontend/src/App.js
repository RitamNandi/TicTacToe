import React, {useState, useEffect} from 'react'
import axios from 'axios'
import Board from './Board'
import './App.css'


function App() {

  const [board, setBoard] = useState([['', '', ''], ['', '', ''], ['', '', '']]);
  const [status, setStatus] = useState('Next player: X');
  const [currentPlayer, setCurrentPlayer] = useState('X');


  useEffect(() => {
    // start a new game
    axios.post('http://127.0.0.1:5000/start')
    .then(response => {
      setBoard(response.data.board);
      setStatus(response.data.message);
    })
    .catch(error => console.error('Error starting game:', error));
  }, []);

  const handleCellClick = (row, col) => {
    // convert row, col to a position 1-9.
    const position = row * 3 + col + 1;
    // post request to move API, pass in player and position
    axios.post('http://127.0.0.1:5000/move' , {
      player: currentPlayer,
      position: position
    })
    .then(response => {
      // get back a board and status
      setBoard(response.data.board);
      setStatus(response.data.status);
      if (currentPlayer === 'X') {
        setCurrentPlayer('O');
      } else {
        setCurrentPlayer('X');
      }
    })
    .catch(error => console.error('Error making move:', error));
  }



  return (
    <div className="app">

      <h1>Tic Tac Toe</h1>
      <Board board={board} onCellClick={handleCellClick} />
      <p>{status}</p>

      
    </div>
  );
}

export default App;