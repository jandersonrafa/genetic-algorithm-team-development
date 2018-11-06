import React, { Component } from "react";

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: "Efetuando Requisição",
    };
  }
  render() {
    const { message } = this.state;
    return (
      <div>
        <h2>Retorno Requisição: {message} </h2>        
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
  componentDidMount() {
    fetch("/api/genetic")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            message: result.message
          });
        },
        (error) => {
          this.setState({
            message: "Erro na requisição",
          });
        }
      )
  }
}

export default Home;