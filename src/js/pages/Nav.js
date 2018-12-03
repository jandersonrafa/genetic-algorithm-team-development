import React, { Component } from "react";
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import Home from "./Home";
import Dev from "./Dev";


class Nav extends Component {
  render() {
    return (
      <HashRouter>
      <div>
        <h1 class='titulo'>IA2: Algoritmo Genético seleção equipe desenvolvimento</h1>
        <ul className="header" class='header'>
          <li><NavLink exact to="/">Home</NavLink> </li>
          <li><NavLink to="/dev">Desenvolvedores</NavLink></li>
        </ul>
        <div className="content">
            <Route exact path="/" component={Home} />
            <Route path="/dev" component={Dev} />
        </div>
      </div>
      </HashRouter>
    );
  }
}

export default Nav;