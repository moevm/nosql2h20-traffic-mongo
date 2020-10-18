import React, { useState } from 'react';
import AntPath from "react-leaflet-ant-path";

const settings = [
    {
        "delay": 200,
        "dashArray": [
            5,
            20
        ],
        "color": "#00FF00",
        "pulseColor": "#FFFFFF"   
    },
    {
        "delay": 400,
        "dashArray": [
            10,
            20
        ],
        "color": "#0000FF",
        "pulseColor": "#FFFFFF"
    },
    {
        "delay": 600,
        "dashArray": [
            10,
            20
        ],
        "color": "#FF000F",
        "pulseColor": "#FFFFFF"
    }
]

function getOptions(index) {
    let s = settings[index];
    return {
        "delay": s["delay"],
        "dashArray": s["dashArray"],
        "weight": 8,
        "color": s["color"],
        "pulseColor": s["pulseColor"],
        "paused": false,
        "reverse": false,
        "hardwareAccelerated": true
    };
}

const Paths = ({paths}) => {
    let listPaths = []
    console.log('WAYS: ', paths);
    console.log(typeof paths);
    paths.forEach( (value, index) => {
        console.log(value, index);
        listPaths.push(<AntPath key={index} positions={value.way} options={getOptions(index)}/>)
    })
    return <>{listPaths}</>
   
    
}

export default Paths;

