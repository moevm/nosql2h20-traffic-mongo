import React, {useEffect, useState} from "react";
import {Table, ToggleButtonGroup, ToggleButton, Spinner} from "react-bootstrap";
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
            data: [10, 10, 10, 10],
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
    let [info, setInfo] = useState({avgTime: "0", avgLevel: 2, data: testData, generalData: [10, 10, 10, 10] })
    let [category, setCategory] = useState(ALL)
    const [isLoading, setIsLoading] = useState(true);

    useEffect( () => {
            fetch(`/api/stat?category=${category}`)
                .then(res => res.json())
                .then(result => {
                    if ("error" in result.data) {
                        alert(result.data["error"])
                    } else {
                        setInfo(result);
                        setIsLoading(false);
                    }
                })
                .catch(err => console.log(err))
        },
        [category])
    return (<MainContainer>
        {
            (() => {
                if (isLoading) {
                    return <Spinner animation="border" role="status">
                        <span className="sr-only">Loading...</span>
                    </Spinner>
                } else {
                    return <>
                        <h1>Статистика пробок на пути</h1>
                        <h2>График </h2>
                        <Pie data={() => {
                            data.datasets[0].data = info.generalData;
                            return data
                        }} options={options}/>
                        <Bar data={() => {
                            data.datasets[0].data = info.generalData;
                            return data
                        }} options={options}/>
                        <h2>Общее время и средний балл пробки</h2>
                        <p><i>avg time</i> - {info.avgTime}</p>
                        <p><i>avg level traffic jam</i> - {info.avgLevel}</p>
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
                    </>
                }
            })()
        }
    </MainContainer>);
}
