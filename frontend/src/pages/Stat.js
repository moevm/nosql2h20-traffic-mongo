import React from "react";
import {Table, ToggleButtonGroup, ToggleButton} from "react-bootstrap";
import MainContainer from "../containers/MainContainer";


export default function Stat() {
    return (<MainContainer>
        <h1>Статистика пробок на пути</h1>
        <h2>График </h2>
        <img src={"https://raw.githubusercontent.com/moevm/nosql2h20-traffic-mongo/master/docs/media/andr_model.jpg"}/>
        <h2>Общее время и средний балл пробки</h2>
        <p>avg time - 7 min 34 sec</p>
        <p>avg level traffic jam - 5.8</p>
        <ToggleButtonGroup type="checkbox">
            <ToggleButton variant="danger" value={1}>NO move almost</ToggleButton>
            <ToggleButton variant="warning" value={2}>Slow</ToggleButton>
            <ToggleButton variant="success" value={3}>Fast</ToggleButton>
            <ToggleButton variant="secondary" value={3}>Reset</ToggleButton>
        </ToggleButtonGroup>
        <br/>
        <br/>
        <Table striped bordered hover>
            <thead>
            <tr>
                <th>#</th>
                <th>id Way</th>
                <th>Coordinate</th>
                <th>Time</th>
                <th>traffic jams level</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td>1</td>
                <td>3124</td>
                <td>175.12 - 1243.312</td>
                <td>3 min 59 sec</td>
                <td>3</td>
            </tr>
            <tr>
                <td>2</td>
                <td>3126</td>
                <td>41243.21312 - 213123.123</td>
                <td>5 min 11 sec</td>
                <td>8</td>
            </tr>
            </tbody>
        </Table>
    </MainContainer>);
}
