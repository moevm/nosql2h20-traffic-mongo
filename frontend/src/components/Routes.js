import React from "react";
import {Route, Switch} from "react-router-dom";
import Home from "../pages/Home";
import Data from "../pages/Data";
import Traffic from "../pages/Traffic";
import Stat from "../pages/Stat";

export default function Routes() {
    return (
        <Switch>
            <Route exact path="/" component={Home}/>
            <Route path="/stat" component={Stat}/>
            <Route path="/traffic" component={Traffic}/>
            <Route path="/data" component={Data}/> 
        </Switch>
    );
}