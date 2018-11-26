import React, { Component } from "react";

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
      developers: []
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
          devs = JSON.parse(result)
          this.setState({
            developers: devs
          });
        },
        (error) => {
          this.setState({
            developers: [],
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
    const { developers } = this.state;

    const listItems = developers.map((d) => <li key={d.name}>{d.salary}</li>);

    return (
      <ul>{developers}</ul> ,

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
        <div>
          {listItems}
        </div>
        <p>
          Cras facilisis urna ornare ex volutpat, et
        convallis erat elementum. Ut aliquam, ipsum vitae
        gravida suscipit, metus dui bibendum est, eget rhoncus nibh
        metus nec massa. Maecenas hendrerit laoreet augue
        nec molestie. Cum sociis natoque penatibus et magnis
        dis parturient montes, nascetur ridiculus mus.
        </p>
        <p>
          Duis a turpis sed lacus dapibus elementum sed eu lectus.
        </p>
      </div>
    );
  }
}

export default Home;