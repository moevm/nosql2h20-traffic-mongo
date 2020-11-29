import React, {useState, createRef,useEffect} from 'react';
import {Map, Marker, Popup} from 'react-leaflet';
import Paths from "./paths";
import {fromIcon, toIcon} from "../Font/Icon";


const InteractiveLayer = () => {
    let [from, setFrom] = useState([59.9190, 30.3078]);
    let [to, setTo] = useState([59.9095, 30.3075]);
    let [rawPath, setRawPath] = useState([{way: [from, to]}]);
    console.log(rawPath)

    let markerFrom = createRef();
    let markerTo = createRef();

    const updatePositionFrom = () => {
        const marker = markerFrom.current;
        if (marker != null) {
            let coordinates = marker.leafletElement.getLatLng();
            setFrom([coordinates.lat, coordinates.lng]);
        }
    }

    useEffect(() => {
        fetch(`/api/map?lon_from=${from[0]}&lat_from=${from[1]}&lon_to=${to[0]}&lat_to=${to[1]}`)
            .then(res => res.json())
            .then(result => {
                if ("error" in result.data) {
                    alert(result.data["error"])
                }
                else {
                    setRawPath(result["path"]);
                    console.log('win');
                }
            })
            .catch(err => {
                console.log('ERROR', err);
            })
    }, [from, to])

    const updatePositionTo = () => {
        const marker = markerTo.current;
        if (marker != null) {
            let coordinates = marker.leafletElement.getLatLng();
            setTo([coordinates.lat, coordinates.lng]);
        }
    }

    return <>
        <Marker position={from} ref={markerFrom} icon={fromIcon} draggable={true} onDragend={updatePositionFrom}>
            <Popup>
                A pretty CSS3 popup. <br /> Easily customizable.
            </Popup>
        </Marker>
        <Marker position={to} ref={markerTo} icon={toIcon} draggable={true} onDragend={updatePositionTo}>
            <Popup>
                A pretty CSS3 popup. <br /> Easily customizable.
            </Popup>
        </Marker>
        <Paths paths={rawPath}/>
    </>

}

export default InteractiveLayer;