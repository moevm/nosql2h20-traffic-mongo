import React,  {useState, useEffect} from "react";
import {Form, FormControl, InputGroup, Table} from "react-bootstrap";
import MainContainer from "../containers/MainContainer";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Button from "react-bootstrap/Button";
import uuid from 'react-uuid'

const testJson = [
    {
        id: 1,
        traffic_jam_level: 2,
        name: "1232"
    },
    {
        id: 2,
        traffic_jam_level: 4,
        name: "1aaa"
    }
]

export default function Traffic() {
    let [min, setMin] = useState(0);
    let [max, setMax] = useState(3);
    let [valueFilter, setValueFilter] = useState(0);
    let [tableData, setTableData] = useState(testJson)

    const updateTable = () => {
        if (!(parseInt(max) >= 3 || parseInt(min) <= 0))
            fetch(`/api/way?way_id=${valueFilter}&min_jam=${min}&max_jam=${max}`)
                .then(res => res.json())
                .then(result => setTableData(result))
                .catch(err => console.log(err))
    }
    return <>
        <MainContainer>
            <br/>
            <h2>Traffic jams levels</h2>
            <br/>
            <Form>
                <Form.Row>
                    <Col>
                        <Form.Control onChange={e => setMin(e.target.value)} placeholder="Min range (default - 0)"/>
                    </Col>
                    <Col>
                        <Form.Control onChange={e => setMax(e.target.value)} placeholder="Max range  (default - 3)"/>
                    </Col>
                </Form.Row>
            </Form>
            <br/>
            <Row>
                <h2>Collection <i>Ways</i></h2>
                <InputGroup className="mb-3">
                    <FormControl onChange={e => setValueFilter(e.target.value)} placeholder="Find way by id"/>
                    <InputGroup.Append>
                        <Button variant="primary" onClick={updateTable}>search</Button>
                    </InputGroup.Append>
                </InputGroup>
            </Row>
            <br/>
            <Table striped bordered hover>
                <thead>
                <tr>
                    <th>#</th>
                    <th>id Way</th>
                    <th>traffic jams level</th>
                    <th>Street Name</th>
                </tr>
                </thead>
                <tbody>
                    {tableData.map((value, index) => {
                        return <tr key={uuid()}>
                            <td>{index}</td>
                            <td>{value.id}</td>
                            <td>{value.traffic_jam_level}</td>
                            <td>{value.name}</td>
                        </tr>
                    })}

                </tbody>
            </Table>
        </MainContainer>
    </>
}
