import sidepanel_style from "@/styles/sidepanel.module.css"
import TheButton from "./TheButton";
import { useEffect } from "react";
import CustomMarker from "./TheMap"

interface TheRoutePanel {
    setRoute: any;
    route: any;
    mapData: any;
};

const TheRoutePanel: React.FC<TheRoutePanel> = ({ setRoute, route, mapData }) => {

    const finishRoute = function () {
        setRoute((pref: boolean) => {
            pref = false
            return pref
        })
    }


    return (
        <>
            {<div style={{ display: route ? 'block' : 'none' }}>
                <div className={sidepanel_style.panel}>
                    {/* <div className={style.name}>
                        */}<h3>Маршрут</h3>{/*
                    </div>
                    <div className={style.description}>
                        <p></p>
                    </div> */}
                    {mapData.markers.map((value: typeof CustomMarker, index:number) => (
                        <p key={index}>{value.name}</p>
                    ))}
                    <TheButton title="Закончить маршрут!" func={finishRoute} />
                </div>
            </div>
            }
        </>
    );
};

export default TheRoutePanel