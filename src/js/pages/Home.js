import React, { Component } from "react";

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      developers: [],
    };
  }
  render() {
    const { developers } = this.state;

    const listItems = developers.map((d) => <li key={d.name}>{d.salary}</li>);

    return (
      <ul>{developers}</ul> ,

      <div>
        <h2>Retorno Requisição:  </h2>
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
  componentDidMount() {
    fetch("/api/genetic")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            developers: JSON.parse(result)
          });
        },
        (error) => {
          this.setState({
            developers: [],
          });
        }
      )
  }
}

export default Home;