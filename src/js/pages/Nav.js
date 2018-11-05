import React, { Component } from "react";
import {
  Route,
  NavLink,
  BrowserRouter
} from "react-router-dom";
import Home from "./Home";
import Blog from "./Blog";
import Contact from "./Contact";


class Nav extends Component {
  render() {
    return (
      <BrowserRouter>
      <div>
        <h1>IA2: Algoritmo Genético seleção equipe desenvolvimento</h1>
        <ul className="header">
          <li><NavLink exact to="/">Home</NavLink> </li>
          <li><NavLink to="/blog">Blog</NavLink></li>
          <li><NavLink to="/contact">Contact</NavLink></li>
        </ul>
        <div className="content">
            <Route exact path="/" component={Home} />
            <Route path="/blog" component={Blog} />
            <Route path="/contact" component={Contact} />
            <Route path="*" component={Home} />
        </div>
      </div>
      </BrowserRouter>
    );
  }
}

export default Nav;