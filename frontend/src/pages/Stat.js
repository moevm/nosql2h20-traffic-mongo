import React from "react";
import MainContainer from "../containers/MainContainer";


export default function Stat() {
    return (<MainContainer>
        <h1>Статистика пробок на пути</h1>
        <h2>График </h2>
        <img src={"https://cloud.pulse19.ru/uploads/2020/10/statistika.-foto-iz-otkrytyh-istochnikov-1068x601.jpg"}/>
        <h2>Общее время и средний балл пробки</h2>
        <p>avg time - 7 min 34 sec</p>
        <p>avf level traffic jam - 5.8</p>
    </MainContainer> );
}
