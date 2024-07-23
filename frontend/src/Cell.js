import React from 'react';
import './Cell.css';

function Cell({ value, onClick }) {
  return (
    <button className="cell" onClick={onClick}>
      {value}
    </button>
  );
}

export default Cell;
