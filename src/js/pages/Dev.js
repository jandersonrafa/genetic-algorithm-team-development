import React, { Component } from "react";

import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
import BootstrapTable from 'react-bootstrap-table-next';

class Dev extends Component {
  constructor(props) {
    super(props);
    this.state = {
      developers: []
    }
  }

  componentDidMount() {

    fetch("/api/developer")
      .then(res => res.json())
      .then(
        (result) => {
          const devs = JSON.parse(result)
          console.log(devs)
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
  }

  render() {
    const { developers } = this.state;
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
      <ul>{developers}</ul> ,

      <div>
        <BootstrapTable keyField='id' data={ developers } columns={ columns } />
      </div>
    );
  }
}

export default Dev;