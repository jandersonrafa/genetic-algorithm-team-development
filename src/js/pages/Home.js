import React, { Component } from "react";

import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
import BootstrapTable from 'react-bootstrap-table-next';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      form: {
        populationSize: {
          value: 10
        },
        numberGenerations: {
          value: 10
        },
        crossoverRate: {
          value: 60
        },
        mutationRate: {
          value: 0.5
        },
        maxMonthlyProjectValue: {
          value: 50000
        }
      },
      individuo: []
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    const params = Object.entries(this.state.form).map(([key, val]) => `${key}=${val.value}`).join('&')

    fetch("/api/genetic?" + params)
      .then(res => res.json())
      .then(
        (result) => {
          const devs = JSON.parse(result)
          console.log(devs)
          this.setState({
            individuo: devs
          });
        },
        (error) => {
          this.setState({
            individuo: [],
          });
        }
      )
    event.preventDefault();
  }

  handleChange(event) {
    const name = event.target.name
    const value = event.target.value

    const updatedControls = {
      ...this.state.form
    };
    const updatedFormElement = {
      ...updatedControls[name]
    };
    updatedFormElement.value = value;

    updatedControls[name] = updatedFormElement;

    this.setState({
      form: updatedControls
    });
  }

  render() {
    const { individuo } = this.state;
    const developers = individuo.combination ? individuo.combination: [];
    console.log(individuo)
    const columns = [{
        dataField: 'name',
        text: 'Nome'
      }, {
        dataField: 'salary',
        text: 'Salário'
      },
      {
        dataField: 'knowledge',
        text: 'Nivel'
      },
      {
        dataField: 'knowledgeValue',
        text: 'Grau conhecimento'
      }
    ];

    return (
      <ul>{individuo}</ul> ,

      <div>
        <h2 class='retorno'>Retorno Requisição:  </h2>

        <form onSubmit={this.handleSubmit} class="form">
          <label>
            <br></br><br></br>
            Tamanho da população:<br></br>
            <input name="populationSize" type="text" value={this.state.form.populationSize.value} onChange={this.handleChange} />
          </label>
          <label>
            <br></br><br></br>
            Número de gerações:<br></br>
            <input name="numberGenerations" type="text" value={this.state.form.numberGenerations.value} onChange={this.handleChange} />
          </label>
          <label>
            <br></br><br></br>
            Taxa de cruzamento(%):<br></br>
            <input name="crossoverRate" type="text" value={this.state.form.crossoverRate.value} onChange={this.handleChange} />
          </label>
          <label>
            <br></br><br></br>
            Taxa de mutação(%):<br></br>
            <input name="mutationRate" type="text" value={this.state.form.mutationRate.value} onChange={this.handleChange} />
          </label>
          <label>
            <br></br><br></br>
            Valor mensal máximo do projeto:<br></br>
            <input name="maxMonthlyProjectValue" type="text" value={this.state.form.maxMonthlyProjectValue.value} onChange={this.handleChange} />
            <br></br><br></br>
          </label>
          <input type="submit" value="Submit" />
        </form>
        <br></br><br></br>
        <label class = "resultado">Total Grau de conhecimento: {individuo.totalKnowledge}
        Total Salários: {individuo.totalSalary}
        </label>
        <BootstrapTable keyField='id' data={ developers } columns={ columns } />

      </div>
    );
  }
}

export default Home;