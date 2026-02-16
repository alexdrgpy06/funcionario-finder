import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [funcionarios, setFuncionarios] = useState([]);

  useEffect(() => {
    fetch('/api/funcionarios')
      .then(response => response.json())
      .then(data => setFuncionarios(data));
  }, []);

  return (
    <div className="App">
      <h1>Funcionarios P%C3%A9blicos en Paraguay</h1>
      <ul>
      {funcionarios.map(funcionario => (
        <li key={funcionario.nombre}>
          <h2>{funcionario.nombre}</h2>
          <p>{funcionario.cargo}</p>
          <p>{funcionario.departamento}</p>
          <p>Salario: {funcionario.salario}</p>
          <h3>Noticias relacionadas</h3>
          <l>
            {funcionario.noticias.map(news => (
              <li key={news.url}>
                <a href={news.url} target=_blank rel="noopener renorrer">
                    {news.title}
                </a>
              </li>
            ))
          }
          </l>
        </li>
      )
    </ul>
    </div>
  );
}

export default App;
