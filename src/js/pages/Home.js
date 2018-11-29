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
    const developers = individuo.combination ? individuo.combination.map((d) => d.developer):[];
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
      text: 'Conhecimento'
    }];

    return (
      <ul>{individuo}</ul> ,

      <div>
        <h2>Retorno Requisição:  </h2>

        <form onSubmit={this.handleSubmit}>
          <label>
            Tamanho da população:
            <input name="populationSize" type="text" value={this.state.form.populationSize.value} onChange={this.handleChange} />
          </label>
          <label>
            Número de gerações:
            <input name="numberGenerations" type="text" value={this.state.form.numberGenerations.value} onChange={this.handleChange} />
          </label>
          <label>
            Taxa de cruzamento(%):
            <input name="crossoverRate" type="text" value={this.state.form.crossoverRate.value} onChange={this.handleChange} />
          </label>
          <label>
            Taxa de mutação(%):
            <input name="mutationRate" type="text" value={this.state.form.mutationRate.value} onChange={this.handleChange} />
          </label>
          <label>
            Valor mensal máximo do projeto:
            <input name="maxMonthlyProjectValue" type="text" value={this.state.form.maxMonthlyProjectValue.value} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Submit" />
        </form>
        Total Grau de conhecimento: {individuo.totalKnowledge}
        Total Salários: {individuo.totalSalary}
        
        <BootstrapTable keyField='id' data={ developers } columns={ columns } />

      </div>
    );
  }
}

export default Home;