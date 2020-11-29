import React, {useState} from "react";
import {Dropdown, Form, Button, FormControl, Spinner} from "react-bootstrap";
import MainContainer from "../containers/MainContainer";
import axios from 'axios';

const NODE = "nodes"
const WAY = "ways"
const RELATION = "relations"


export default function Data() {
    const [file, setFile] = useState("");
    const [typeCollection, setTypeCollection] = useState(NODE)
    const [isLoading, setIsLoading] = useState(false);

    const onFileChange = event => {
        setFile(event.target.files[0]);
    };

    const onFileUpload = () => {
        const formData = new FormData();
        formData.append(
            typeCollection,
            file,
            file.name
        );
        setIsLoading(true);

        axios.post("/api/bd", formData).then(res => {
            console.log(res.data);
            console.log(res.data["error"]);
            console.log("error" in res.data);
            if ("error" in res.data) {
                alert(res.data["error"])
                setIsLoading(false);
            } else {
                console.log(res.status);
                setIsLoading(false);
            }

        });
    };


    return (<MainContainer>
        <Form>
            <br/>
            <h2>Import</h2>
            <br/>
            <Button variant={"success"} onClick={onFileUpload}>
                Import
            </Button>
            <br/>
            <br/>
            <Dropdown>
                <Dropdown.Toggle variant="primary" id="dropdown-basic">
                    {typeCollection}
                </Dropdown.Toggle>

                <Dropdown.Menu>
                    <Dropdown.Item onClick={() => setTypeCollection(NODE)}>{NODE}</Dropdown.Item>
                    <Dropdown.Item onClick={() => setTypeCollection(WAY)}>{WAY}</Dropdown.Item>
                    <Dropdown.Item onClick={() => setTypeCollection(RELATION)}>{RELATION}</Dropdown.Item>
                </Dropdown.Menu>
            </Dropdown>
            <br/>
            <FormControl
                type="file"
                onChange={onFileChange}/>


            <h2>Export</h2>
            <a href={"api/bd"} target="_blank" rel="noopener noreferrer" download>
                <Button>
                    <i className="fas fa-download"/>
                    Download File
                </Button>
            </a>
        </Form>
        {
            (() => {
               if(isLoading)
                   return <Spinner animation="border" role="status">
                       <span className="sr-only">Loading...</span>
                   </Spinner>
            })()
        }
    </MainContainer>)
}
