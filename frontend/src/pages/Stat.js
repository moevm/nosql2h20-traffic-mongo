import React, {useEffect, useState} from "react";
import {Table, ToggleButtonGroup, ToggleButton} from "react-bootstrap";
import MainContainer from "../containers/MainContainer";
import {Bar, Pie} from '@reactchartjs/react-chart.js'
import uuid from 'react-uuid'

const NO_MOVE = 0
const SLOW = 1
const NORMAL = 2
const ALL = 3

let data = {
    labels: [0, 1, 2, 3],
    datasets: [
        {
            label: 'Traffic jam level',
            data: [12, 19, 3, 5],
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 2,
        },
    ],
}

const options = {
    scales: {
        yAxes: [
            {
                ticks: {
                    beginAtZero: true,
                },
            },
        ],
    },
}


const testData = [
    {
        id: 1,
        time: "sdsa",
        trafficJamLevel: 3
    },
    {
        id: 2,
        time: "sdsaf",
        trafficJamLevel: 34
    }
]

export default function Stat() {
    let [info, setInfo] = useState({avgTime: "0", avgLevel: 2, data: testData, generalData: [12, 10, 3, 5] })
    let [category, setCategory] = useState(ALL)

    useEffect( () => {
            fetch(`/api/stat?category=${category}`)
                .then(res => res.json())
                .then(result => setInfo(result))
                .catch(err => console.log(err))
        },
        [category])
    return (<MainContainer>
        <h1>Статистика пробок на пути</h1>
        <h2>График </h2>
        <Pie data={() => {
            data.datasets[0].data = info.generalData;
            return data
        }} options={options}/>
        <h2>Общее время и средний балл пробки</h2>
        <p>avg time - {info.avgTime}</p>
        <p>avg level traffic jam - {info.avgLevel}</p>
        <ToggleButtonGroup type="checkbox">
            <ToggleButton variant="danger" onChange={() => setCategory(NO_MOVE)} value={NO_MOVE}>NO move almost</ToggleButton>
            <ToggleButton variant="warning" onChange={() => setCategory(SLOW)} value={SLOW}>Slow</ToggleButton>
            <ToggleButton variant="success" onChange={() => setCategory(NORMAL)} value={NORMAL}>Fast</ToggleButton>
            <ToggleButton variant="secondary" onChange={() => setCategory(ALL)} value={ALL}>Reset</ToggleButton>
        </ToggleButtonGroup>
        <br/>
        <br/>
        <Table striped bordered hover>
            <thead>
            <tr>
                <th>#</th>
                <th>id Way</th>
                <th>Time</th>
                <th>traffic jams level</th>
            </tr>
            </thead>
            <tbody>
            {info.data.map((value, index) => {
                return <tr key={uuid()}>
                    <td>{index}</td>
                    <td>{value.id}</td>
                    <td>{value.time}</td>
                    <td>{value.trafficJamLevel}</td>
                </tr>
            })}

            </tbody>
        </Table>
    </MainContainer>);
}
